from datetime import datetime, timedelta
from io import StringIO

import grow_recipe


def test_get_metric():

    xml = StringIO(
        '''
        <recipe>
          <germination duration="1">
            <air>
              <temperature min="26" max="30" />
            </air>
          </germination>
          <vegetative duration="1">
            <air>
              <temperature min="22" max="25" />
            </air>
          </vegetative>
        </recipe>
        '''
    )

    timestamp = datetime.utcnow()

    t9e = grow_recipe.get_metric(
        xml,
        grow_recipe.constants.AIR,
        grow_recipe.constants.T9E,
        timestamp,
        timestamp + timedelta(seconds=1)
    )

    assert t9e.min == 22.0
    assert t9e.max == 25.0


def test_default():
    xml = StringIO(
        '''
        <recipe>
          <default>
            <air>
              <temperature min="26" max="30" />
            </air>
          </default>
        </recipe>
        '''
    )

    timestamp = datetime.utcnow()

    t9e = grow_recipe.get_metric(
        xml,
        grow_recipe.constants.AIR,
        grow_recipe.constants.T9E,
        timestamp
    )

    assert t9e.min == 26.0
    assert t9e.max == 30.0
