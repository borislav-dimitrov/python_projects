import screen_brightness_control as sbc


class Monitor:
    def __init__(self, monitor_id: int, monitor_name: str):
        self.monitor_id = monitor_id
        self.monitor_name = monitor_name

    def set_brightness(self, brightness_level: int):
        sbc.set_brightness(value=brightness_level, display=self.monitor_name)

    @property
    def brightness(self) -> int:
        return sbc.get_brightness(display=self.monitor_id)[0]

    @property
    def brightness_level(self) -> list[int | None]:
        return sbc.get_brightness(monitor=self.monitor_name)


class BrightnessController:
    def __init__(self) -> None:
        self._monitors: list[Monitor] = []
        self.min_brightness = 0
        self.max_brightness = 100

        self.detected_monitors()

    def detected_monitors(self) -> None:
        self._monitors.clear()
        detected_monitors = sbc.list_monitors()

        for idx, monitor in enumerate(detected_monitors):
            self._monitors.append(Monitor(monitor_id=idx, monitor_name=monitor))

    @staticmethod
    def set_brightness(brightness_level: int, monitor: Monitor | None = None) -> None:
        if monitor:
            monitor.set_brightness(brightness_level)
        else:
            sbc.set_brightness(brightness_level)

    @staticmethod
    def get_monitor_brightness(monitor: Monitor) -> int:
        return sbc.get_brightness(display=monitor.monitor_id)[0]

    @property
    def monitors(self) -> list[Monitor | None]:
        return self._monitors