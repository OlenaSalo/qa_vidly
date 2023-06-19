
from typing import Optional, Union, Callable, Tuple, Dict, List, Any

from selene.common.none_object import _NoneObject
from selenium.webdriver.firefox.webdriver import WebDriver


class Configuration:

    def __init__(
            self,
            driver: Optional[Union[WebDriver, Callable[[], WebDriver]]] = None,
            timeout: int = 4,
            base_url: str = '',
            window_width: Optional[int] = None,
            window_height: Optional[int] = None,
    ):
        self._driver = driver
        self._timeout = timeout
        self._base_url = base_url
        self._window_width = window_width
        self._window_height = window_height


    @property
    def driver(self) -> Union[WebDriver, _NoneObject]:
        return (
            self._driver
            if isinstance(self._driver, WebDriver)
            else (
                self._driver()
                if callable(self._driver)
                else _NoneObject(
                    'expected Callable[[], WebDriver] inside property config.driver'
                )
            )
        )

    @property
    def timeout(self) -> int:
        return self._timeout


    @property
    def base_url(self) -> str:
        return self._base_url


    @property
    def window_width(self) -> Optional[int]:
        return self._window_width

    @property
    def window_height(self) -> Optional[int]:
        return self._window_height
