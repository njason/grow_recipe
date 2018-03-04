from datetime import datetime

from lxml import etree

from grow_recipe import constants, validate


class Metric:

    def __init__(self, min_value=None, max_value=None):
        self.min = min_value
        if self.min:
            self.min = float(self.min)

        self.max = max_value
        if self.max:
            self.max = float(self.max)


class QueryValueError(ValueError):
    pass


def get_grow_stage(xml, start_time, query_time=None):
    """
    Attempts to find a stage based on the how much time has elapsed since the
    beginning of the grow
    """

    if validate.valid(xml):
        # go back to the beginning
        xml.seek(0)

        tree = etree.parse(xml)

        if not query_time:
            query_time = datetime.utcnow()

        if start_time > query_time:
            raise QueryValueError('start_time is after query_time')

        seconds_diff = (query_time - start_time).seconds

        root = tree.xpath('/{root}'.format(root=constants.ROOT_NODE)).pop()

        # keeps track of the cumulative amount of seconds while checking
        # each stage
        time_counter = 0

        for stage in root.getchildren():

            if stage.tag == constants.Stages.DEFAULT.value:
                continue

            duration_str = stage.attrib.get('duration')
            if duration_str is None:
                continue
            duration = int(duration_str)

            if seconds_diff < time_counter + duration:
                return constants.Stages(stage.tag)

            time_counter += duration


def find_metric_value(xml, stage, topic, metric):
    """
    Finds the specified metric in the given stage. If the metric is not
    present in the given stage, the metric is taken from the default stage
    """

    if validate.valid(xml):
        # go back to the beginning
        xml.seek(0)

        tree = etree.parse(xml)

        if not stage:
            stage = constants.Stages.DEFAULT.value

        value = tree.xpath('/{root}/{stage}/{topic}/{metric}'
                           .format(root=constants.ROOT_NODE, stage=stage,
                                   topic=topic, metric=metric))

        if not value:
            value = tree.xpath('/{root}/{stage}/{topic}/{metric}'.format(
                root=constants.ROOT_NODE,
                stage=constants.Stages.DEFAULT.value, topic=topic,
                metric=metric))

        if not value:
            return None

        # there should only be definition if the metric is present
        assert len(value) == 1

        return Metric(value[0].attrib.get('min'),
                      value[0].attrib.get('max'))
