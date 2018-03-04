from datetime import datetime, timedelta
from io import StringIO
from unittest import TestCase

from grow_recipe import constants, query


class TestGetGrowStage(TestCase):

    def test_basic(self):
        xml = StringIO( '<recipe>'
                            '<germination duration="1"></germination>'
                        '</recipe>'
                       )

        timestamp = datetime.utcnow()

        stage = query.get_grow_stage(xml, timestamp, timestamp)

        assert stage == constants.Stages.GERMINATION

    def test_second_stage(self):
        xml = StringIO( '<recipe>'
                            '<germination duration="1"></germination>'
                            '<vegetative duration="1"></vegetative>'
                        '</recipe>'
                       )

        timestamp = datetime.utcnow()

        stage = query.get_grow_stage(xml, timestamp,
                                     timestamp + timedelta(seconds=1))

        assert stage == constants.Stages.VEGETATIVE

    def test_grow_time_out_of_range(self):
        xml = StringIO( '<recipe>'
                            '<default></default>'
                            '<germination duration="1"></germination>'
                        '</recipe>'
                       )

        timestamp = datetime.utcnow()

        stage = query.get_grow_stage(xml, timestamp,
                                     timestamp + timedelta(seconds=1))

        assert not stage

    def test_no_duration_specified(self):
        xml = StringIO( '<recipe>'
                            '<germination></germination>'
                        '</recipe>'
                       )

        timestamp = datetime.utcnow()

        stage = query.get_grow_stage(xml, timestamp, timestamp)

        assert not stage


class TestFindMetricValue(TestCase):

    def test_basic(self):
        xml = StringIO( '<recipe>'
                            '<germination>'
                                '<air>'
                                    '<temperature min="20" max="25" />'
                                '</air>'
                            '</germination>'
                        '</recipe>'
                       )

        temperature = query.find_metric_value(xml, 'germination', 'air',
                                              'temperature')

        assert temperature.min == 20.0
        assert temperature.max == 25.0

    def test_default(self):
        xml = StringIO( '<recipe>'
                            '<default>'
                                '<air>'
                                    '<temperature min="20" max="25" />'
                                '</air>'
                            '</default>'
                        '</recipe>'
                       )

        temperature = query.find_metric_value(xml, 'germination', 'air',
                                              'temperature')

        assert temperature.min == 20.0
        assert temperature.max == 25.0


    def test_override(self):
        xml = StringIO( '<recipe>'
                            '<default>'
                                '<air>'
                                    '<temperature min="20" max="25" />'
                                '</air>'
                            '</default>'
                            '<germination>'
                                '<air>'
                                    '<temperature min="30" max="35" />'
                                '</air>'
                            '</germination>'
                        '</recipe>'
                       )

        temperature = query.find_metric_value(xml, 'germination', 'air',
                                              'temperature')

        assert temperature.min == 30.0
        assert temperature.max == 35.0


    def test_no_stage(self):
        xml = StringIO( '<recipe>'
                            '<default>'
                                '<air>'
                                    '<temperature min="20" max="25" />'
                                '</air>'
                            '</default>'
                            '<germination>'
                                '<air>'
                                    '<temperature min="30" max="35" />'
                                '</air>'
                            '</germination>'
                        '</recipe>'
                       )

        temperature = query.find_metric_value(xml, None, 'air', 'temperature')

        assert temperature.min == 20.0
        assert temperature.max == 25.0
