from drf_yasg import openapi

location_id = openapi.Parameter(
    'location_id', openapi.IN_QUERY,
    description="Query param location_id", type=openapi.TYPE_NUMBER
)

surname = openapi.Parameter(
    'surname', openapi.IN_QUERY,
    description="Query param surname", type=openapi.TYPE_STRING
)

department_id = openapi.Parameter(
    'department_id', openapi.IN_QUERY,
    description="Query param department_id", type=openapi.TYPE_NUMBER
)
