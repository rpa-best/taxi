from django.contrib.gis.forms.widgets import OSMWidget


class GeoWidget(OSMWidget):
    default_lon = 30.3141
    default_lat = 59.9386

    class Media:
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/ol3/4.6.5/ol.css",
                "gis/css/ol3.css",
            )
        }
        js = (
            "https://cdnjs.cloudflare.com/ajax/libs/ol3/4.6.5/ol.js",
            "gis/js/OLMapWidget.js",
        )