from homeassistant.components.climate.const import (
    HVACMode,
    FAN_LOW,
    FAN_HIGH
)

VALID_MODES = {
    "0": HVACMode.COOL,
#    "1": HVACMode.HEAT,
    "2": HVACMode.AUTO,
#    "3": HVACMode.FAN_ONLY,
#    "4": HVACMode.DRY,
    "5": HVACMode.OFF,
}

FAN_MODES = {
    "1": FAN_LOW,
    "3": FAN_HIGH,
}
