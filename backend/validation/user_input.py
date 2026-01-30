from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal, Optional


class user_input(BaseModel):
    State_Name: Annotated[
        Literal[
            "andhra pradesh",
            "arunachal pradesh",
            "assam",
            "bihar",
            "goa",
            "gujarat",
            "haryana",
            "jammu and kashmir",
            "karnataka",
            "kerala",
            "madhya pradesh",
            "maharashtra",
            "manipur",
            "meghalaya",
            "mizoram",
            "nagaland",
            "odisha",
            "punjab",
            "rajasthan",
            "tamil nadu",
            "telangana",
            "uttar pradesh",
            "west bengal",
            "chandigarh",
            "dadra and nagar haveli",
            "himachal pradesh",
            "puducherry",
            "sikkim",
            "tripura",
            "andaman and nicobar islands",
            "chhattisgarh",
            "uttarakhand",
            "jharkhand",
        ],
        Field(
            ...,
            title="Name of the State",
            description="Select the name of the state you want the yeild of the crop",
        ),
    ]
    Crop_Type: Annotated[
        Optional[Literal["kharif", "rabi", "summer", "whole year"]],
        Field(
            title="Type of the crop",
            description="Select the type of the crop based on growing season",
        ),
    ]
    Crop: Annotated[
        Literal[
            "cotton",
            "horsegram",
            "jowar",
            "maize",
            "moong",
            "ragi",
            "rice",
            "sunflower",
            "wheat",
            "sesamum",
            "soyabean",
            "rapeseed",
            "jute",
            "arecanut",
            "onion",
            "potato",
            "sweetpotato",
            "tapioca",
            "turmeric",
            "barley",
            "banana",
            "coriander",
            "garlic",
            "blackpepper",
            "cardamom",
            "cashewnuts",
            "ladyfinger",
            "brinjal",
            "grapes",
            "mango",
            "orange",
            "tomato",
            "papaya",
            "pineapple",
            "cabbage",
        ],
        Field(
            ...,
            title="Name of the crop",
            description="Select the name of the crop you want the yeild of",
        ),
    ]
    N: Annotated[
        float,
        Field(
            ...,
            title="Nitrogen amount in soil",
            description="Give the amount of nitrogen present in the soil at that particular place",
        ),
    ]
    P: Annotated[
        float,
        Field(
            ...,
            title="Phosphorus amount in soil",
            description="Give the amount of Phosphorus present in the soil at that particular place",
        ),
    ]
    K: Annotated[
        float,
        Field(
            ...,
            title="Potassium amount in soil",
            description="Give the amount of Potassium present in the soil at that particular place",
        ),
    ]
    pH: Annotated[
        float,
        Field(
            ...,
            title="ph amount in soil",
            description="Enter the amount of ph in the soil of your desired location",
        ),
    ]
    rainfall: Annotated[
        float,
        Field(
            ...,
            title="average rainfall",
            description="Enter the average rainfall in centimeters",
        ),
    ]
    temperature: Annotated[
        float,
        Field(
            ...,
            title="average temperature",
            description="Enter the average temperature of the desired location",
        ),
    ]

    # @computed_field
    # @property
    # def npk_sum(self) -> float:
    #     return self.N + self.P + self.K

    # @computed_field
    # @property
    # def n_to_p_ratio(self) -> float:
    #     return self.N / (self.P + 1)

    # @computed_field
    # @property
    # def n_to_k_ratio(self) -> float:
    #     return self.N / (self.K + 1)

    # @computed_field
    # @property
    # def p_to_k_ratio(self) -> float:
    #     return self.P / (self.K + 1)

    # @computed_field
    # @property
    # def ph_optimal(self) -> int:
    #     is_optimal = (self.pH >= 6.0) & (self.pH <= 7.5)
    #     if is_optimal == True:
    #         return 1
    #     return 0

    # @computed_field
    # @property
    # def ph_distance(self) -> float:
    #     return abs(self.pH - 6.5)

    # @computed_field
    # @property
    # def ph_squared(self) -> float:
    #     return self.pH**2

    # @computed_field
    # @property
    # def rainfall_temp(self) -> float:
    #     return self.rainfall * self.temperature

    # @computed_field
    # @property
    # def water_stress(self) -> float:
    #     return self.temperature / (self.rainfall + 1)
