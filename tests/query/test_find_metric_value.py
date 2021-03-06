from io import StringIO

from grow_recipe import constants, find_metric_value


def test_basic():
    xml = StringIO(
        '''
        <recipe>
          <germination>
            <air>
              <temperature min="20" max="25" />
            </air>
          </germination>
        </recipe>
        '''
    )

    temperature = find_metric_value(
        xml, constants.GERMINATION, constants.AIR, constants.T9E)

    assert temperature.min == 20.0
    assert temperature.max == 25.0


def test_default():
    xml = StringIO(
        '''
        <recipe>
          <default>
            <air>
              <temperature min="20" max="25" />
            </air>
          </default>
        </recipe>
        '''
    )

    temperature = find_metric_value(
        xml, constants.GERMINATION, constants.AIR, constants.T9E)

    assert temperature.min == 20.0
    assert temperature.max == 25.0


def test_override():
    xml = StringIO(
        '''
        <recipe>
          <default>
            <air>
              <temperature min="20" max="25" />
            </air>
          </default>
          <germination>
            <air>
              <temperature min="30" max="35" />
            </air>
          </germination>
        </recipe>
        '''
    )

    temperature = find_metric_value(
        xml, constants.GERMINATION, constants.AIR, constants.T9E)

    assert temperature.min == 30.0
    assert temperature.max == 35.0


def test_no_stage():
    xml = StringIO(
        '''
        <recipe>
          <default>
            <air>
              <temperature min="20" max="25" />
            </air>
          </default>
          <germination>
            <air>
              <temperature min="30" max="35" />
            </air>
          </germination>
        </recipe>
        '''
    )

    temperature = find_metric_value(
        xml, None, constants.AIR, constants.T9E)

    assert temperature.min == 20.0
    assert temperature.max == 25.0
