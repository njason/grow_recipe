from datetime import datetime, timedelta
from io import StringIO

from grow_recipe import constants, get_grow_stage


def test_basic():
    xml = StringIO(
        '''
        <recipe>
          <germination duration="1"></germination>
        </recipe>
        '''
    )

    timestamp = datetime.utcnow()

    stage = get_grow_stage(xml, timestamp, timestamp)

    assert stage == constants.Stages.GERMINATION


def test_second_stage():
    xml = StringIO(
        '''
        <recipe>
          <germination duration="1"></germination>
          <vegetative duration="1"></vegetative>
        </recipe>
        '''
    )

    timestamp = datetime.utcnow()

    stage = get_grow_stage(
        xml, timestamp, timestamp + timedelta(seconds=1))

    assert stage == constants.Stages.VEGETATIVE


def test_grow_time_out_of_range():
    xml = StringIO(
        '''
        <recipe>
          <default></default>
          <germination duration="1"></germination>
        </recipe>
        '''
    )

    timestamp = datetime.utcnow()

    stage = get_grow_stage(
        xml, timestamp, timestamp + timedelta(seconds=1))

    assert not stage


def test_no_duration_specified():
    xml = StringIO(
        '''
        <recipe>
          <germination></germination>
        </recipe>
        '''
    )

    timestamp = datetime.utcnow()

    stage = get_grow_stage(
        xml, timestamp, timestamp)

    assert not stage
