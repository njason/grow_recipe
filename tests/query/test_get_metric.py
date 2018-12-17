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

    temperature = grow_recipe.get_metric(
        xml,
        grow_recipe.constants.Topics.AIR.value,
        grow_recipe.constants.Metrics.TEMPERATURE.value,
        timestamp,
        timestamp + timedelta(seconds=1)
    )

    assert temperature.min == 22.0
    assert temperature.max == 25.0
