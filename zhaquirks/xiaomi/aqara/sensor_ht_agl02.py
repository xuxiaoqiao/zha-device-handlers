"""Xiaomi aqara weather sensor device."""
import logging

from zigpy.profiles import zha
from zigpy.zcl.clusters.general import Identify, Ota
from zigpy.zcl.clusters.measurement import PressureMeasurement

from zhaquirks import Bus
from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.xiaomi import (
    LUMI,
    BasicCluster,
    PressureMeasurementCluster,
    RelativeHumidityCluster,
    TemperatureMeasurementCluster,
    XiaomiAqaraE1Cluster,
    XiaomiCustomDevice,
    XiaomiPowerConfiguration,
)

_LOGGER = logging.getLogger(__name__)


class Weather(XiaomiCustomDevice):
    """Xiaomi weather sensor device."""

    def __init__(self, *args, **kwargs):
        """Init."""
        self.temperature_bus = Bus()
        self.humidity_bus = Bus()
        self.pressure_bus = Bus()
        super().__init__(*args, **kwargs)

    signature = {
        #  <SimpleDescriptor endpoint=1 profile=260 device_type=24321
        #  device_version=1
        #  input_clusters=[0, 3, 65535, 1026, 1027, 1029]
        #  output_clusters=[0, 4, 65535]>
        MODELS_INFO: [(LUMI, "lumi.sensor_ht.agl02")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.TEMPERATURE_SENSOR,
                INPUT_CLUSTERS: [
                    BasicCluster.cluster_id,
                    XiaomiPowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    TemperatureMeasurementCluster.cluster_id,
                    PressureMeasurement.cluster_id,
                    RelativeHumidityCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            }
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                INPUT_CLUSTERS: [
                    BasicCluster,
                    XiaomiPowerConfiguration,
                    Identify.cluster_id,
                    TemperatureMeasurementCluster,
                    PressureMeasurementCluster,
                    RelativeHumidityCluster,
                    XiaomiAqaraE1Cluster,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            }
        },
    }
