import math
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from MAVProxy.modules.mavproxy_console import ConsoleModule


@pytest.mark.parametrize(
    "yaw_deg",
    [-180, -90, 0, 90, 180]
)
def test_yaw_is_displayed_in_degrees(yaw_deg):
    fake_console = Mock()
    fake_module = SimpleNamespace(console=fake_console)

    msg = SimpleNamespace(
        roll=0.0,
        pitch=0.0,
        yaw=math.radians(yaw_deg)
    )

    ConsoleModule.handle_attitude(fake_module, msg)

    fake_console.set_status.assert_any_call(
        "Yaw", f"Yaw {yaw_deg}"
    )
