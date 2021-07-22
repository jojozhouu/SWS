# PRODUCTION templates

## Representing Resources

| Resource  | Notes       |
| --------  | -----       |
| R1        | Available Land |
| R2        | [Water](#housing-template) |
| R3        | [Housing](#housing-template) |
| R4        | [Metals](#metals-template) |
| R5        | [Timber](#timber-template) |
| R6        | [Forest](#forestation-template) |
| R7        | [Potential Fossil Energy](#potential-fossil-energy-extraction-template) |
| R8        | [Farm Land](#farm-land-template) |
| R9        | [Population](#reproduction-template)|
| R10       | [Crop](#crop-production-template) |
| R11       | [Meat](#meat-production-template) |
| R12       | [Potential Fossil Energy Usable](#potential-fossil-energy-extraction-template)|
| R13       | [Potential Renewable Energy Usable](#potential-renewable-energy-extraction-template) |
| R14       | [Metallic Alloys](#alloys-template) |
| R15       | [Electronics](#electronics-template) |
| R16       | [Military](#military-resource-creation-template) |
| R17       | Military Population |
| R3'       | [Housing Waste](#waste-management-templates) |
| R8'       | [Farm Land Waste](#waste-management-templates) |
| R9'       | [Population Waste](#waste-management-templates) |
| R11'      | [Meat Waste](#waste-management-templates) |
| R12'      | [Fossil Energy Waste](#waste-management-templates) |
| R13'      | [Renewable Energy Waste](#waste-management-templates) |
| R14'      | [Metallic Alloy Waste](#waste-management-templates) |
| R15'      | [Electronics Waste](#waste-management-templates) |
| RR'       | [Carbon footprint](#forestation-template) |

Unit Measurements:
1. Timber: 1 ton / unit
1. Water: 1 ton / unit
1. Crop: 1 ton / unit
1. Meat: 1 ton / unit
1. Carbon Footprint: 1 ton / unit
1. Waste: 1 ton / unit
1. Available Land: 1 acre / unit
1. Forest: 1 acre / unit

### Metals Template
```
(PRODUCTION ?C
            (INPUTS (Population 2)
                    (AvailableLand 1))
            (OUTPUTS (Metals 20)
                     (AvailableLand 0)
                     (Population 2)))
```

### Timber Template
```
(PRODUCTION ?C
            (INPUTS (Population 4)
                    (Forest 1)
            (OUTPUTS (Timber 90)
                     (AvailableLand 1)
                     (Population 4)))
```
#### Source:
1. https://www.forest2market.com/blog/how-many-tons-of-wood-are-on-an-acre-of-land#:~:text=Forest2Market%20data%20from%20timberland%20type,clearcut%3A%2099%20tons%20per%20acre

### Alloys Template
```
(PRODUCTION ?C
            (INPUTS (Population 1)
                    (Metals 2)
                    (Water 3))
            (OUTPUTS (MetallicAlloys 1)
                     (MetallicAlloysWaste 1)
                     (Population 1)))
```

### Electronics Template
```
(PRODUCTION ?C
            (INPUTS (Population 1)
                    (Metals 3)
                    (MetallicAlloys 2)
                    (PotentialEnergyUsable 3)
                    (Water 3))
            (OUTPUTS (Electronics 2)
                     (ElectronicsWaste 1)
                     (Population 1)))
```

### Housing Template
```
(PRODUCTION ?C
            (INPUTS (Population 5)
                    (Metals 1)
                    (Timber 5)
                    (MetallicAlloys 3)
                    (AvailableLand 1)
                    (Water 5)
                    (PotentialEnergyUsable 5))
            (OUTPUTS (Housing 1)
                     (HousingWaste 1)
                     (Population 5)))
```

### Farm Land Template
```
(PRODUCTION ?C
            (INPUTS (Population 4)
                    (AvailableLand 1))
            (OUTPUTS (AvailableLand 0)
                     (FarmLand 1)
                     (FarmWaste 0.1)
                     (Population 4)))
```

### Crop Production Template
```
(PRODUCTION ?C
            (INPUTS (Population 4)
                    (FarmLand 1)
                    (Water 40))
            (OUTPUTS (Crop 13)
                     (FarmLand 1)
                     (FarmWaste 0.2)
                     (Water 40)
                     (Population 4)))
```
#### Reasoning:
1. We use information about potato to model this template since potato is one of the highest yield base crops.
1. Potatoes need 2 inches of water per acre week, and they take about 13 weeks to mature on average. Therefore, we need 2 (acre * inch) * 13 = 26 (acre * inch) = 3,629 (cubic ft) = 40 tons of water.
1. Water is eventually renewable. Therefore, the amount of water in the output is the same as that in the input.
1. We are separating vegetables and meat production because meat production is a major source of green house gases, which has a considerably higher impact on a country's carbon footprint.

#### Source
1. https://www.gardendesign.com/vegetables/potatoes.html#:~:text=Small%20new%20potatoes%20can%20be,100%20days%20to%20reach%20maturity


### Meat Production Template
```
(PRODUCTION ?C
            (INPUTS (Population 1)
                    (FarmLand 5)
                    (Water 220)
                    (Crop 70))
            (OUTPUTS (Meat 4)
                     (FarmLand 5)
                     (FarmWaste 1)
                     (MeatWaste 1)
                     (CarbonFootprint 1.8)
                     (Water 220)
                     (Population 1)))
```
#### Reasoning
1. Meat constitutes a major part of the modern diet. We base our template on beef production.
1. We can expect a yield of 880 pounds per cattle.
1. A cattle consumes 24 pounds of food per day, 10 gallons of water per day. A cattle finishes around 20 months of age. Therefore, we need about 22 units of water and and 7 units of crop.
1. A cattle belch 220 pounds of methane per year. Therefore, a cattle belch about 370 pounds = 0.18 tons in its lifetime.
1. 1 person can comfortably manage 5 acre cattle farm with 10 animals.
1. Not all parts of the animal can be consumed (i.e., bones, offals). The unusable parts of the animal are reflected by MeatWaste.

#### Source
1. https://beef.unl.edu/beefwatch/2020/how-many-pounds-meat-can-we-expect-beef-animal
1. https://beef.unl.edu/cattleproduction/forageconsumed-day#:~:text=As%20an%20example%2C%20if%20it,on%20an%20as%2Dfed%20basis
1. https://extension.oregonstate.edu/animals-livestock/beef/looking-forward-beef-harvest#:~:text=Your%20job%20will%20be%20to,over%2030%20months%20of%20age
1. https://www.ucdavis.edu/food/news/making-cattle-more-sustainable/#:~:text=1%20agricultural%20source%20of%20greenhouse,the%20Department%20of%20Animal%20Science


### Potential Fossil Energy Extraction Template
```
(PRODUCTION ?C
            (INPUTS (Population 5)
                    (MetallicAlloys 5)
                    (PotentialFossilEnergy 10)
                    (AvailableLand 1))
            (OUTPUTS (PotentialFossilEnergy 0)
                     (PotentialFossilEnergyUsable 8)
                     (PotentialFossilEnergyUsableWaste 2)
                     (AvailableLand 1)
                     (MetallicAlloys 0)
                     (Population 5)))
```

#### Reasoning
1. Only 83% of crude oil is used to provide energy. The rest is turned into other products. This value is rounded to 80% in the template.

#### Source:
1. https://www.breakthroughfuel.com/blog/crude-oil-barrel/

### Potential Renewable Energy Extraction Template
```
(PRODUCTION ?C
            (INPUTS (Population 8)
                    (MetallicAlloys 5)
                    (Electronics 5)
                    (AvailableLand 1))
            (OUTPUTS (PotentialRenewableEnergyUsable 10)
                     (PotentialRenewableEnergyUsableWaste 1)
                     (MetallicAlloys 0)
                     (Electronics 0)
                     (AvailableLand 0)
                     (Population 8)))
```

#### Note:
1. We might need to adjust the PotentialRenewableEnergyUsable such that the use of renewable energy produces a higher state quality score than that of fossil energy.
2. There should not be additional when using renewable energy.

#### Reasoning:
1. We are not using potential renewable energy because renewable energy are, by definition, infinite.
2. The expensiveness of extracting potential renewable energy is reflected in the use of electronics and available land.


### Waste Management Templates
1. Burning waste:
```
(PRODUCTION ?C
            (INPUTS (Population 4)
                    (Waste 10)
                    (AvailableLand 1))
            (OUTPUTS (CarbonFootprint 3)
                     (Waste 0)
                     (AvailableLand 1)
                     (Population 4)))
```
2. Landfill:
```
(PRODUCTION ?C
            (INPUTS (Population 4)
                    (Waste 35)
                    (AvailableLand 0.1))
            (OUTPUTS (CarbonFootprint 35)
                     (Waste 0)
                     (AvailableLand 0)
                     (Population 4)))
```

#### Note
1. The use of these templates are based on the assumption that unprocessed waste results in a lower state quality score than carbon footprint.
1. Burning only applies to a few categories of wastes. All waste can be put into landfill.
1. Waste doesn't need to reach the specified amount to be burnt or be put in landfill. The output carbon footprint changes proportionally, but other resources remain unchanged when the waste is less than specified in the templates.

#### Reasoning
1. U.S. Landfills hold about 140 million tons of waste, and produces about 148 million metric tons of CO2 equivalent. Therefore, 1 unit of waste produces 1 unit of carbon footprint.

#### Source
1. https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references
1. https://www.dumpsters.com/blog/us-trash-production#:~:text=Every%20year%2C%20U.S.%20landfills%20are,tons%20of%20paper%20and%20paperboard
1. https://ensia.com/features/methane-landfills/#:~:text=U.S.%20landfills%20released%20an%20estimated,a%20capacity%20of%202%2C163%20megawatts
1. https://scdhec.gov/environment/land-and-waste-landfills/how-landfills-work#:~:text=On%20average%2C%20about%201%2C200%20to,one%20cubic%20yard%20of%20space

### Forestation Template
```
(PRODUCTION ?C
            (INPUTS (Population 10)
                    (Water 30)
                    (AvailableLand 1)
                    (CarbonFootprint 2.5))
            (OUTPUTS (CarbonFootprint 0)
                     (AvailableLand 0)
                     (Forest 1)
                     (Water 30)
                     (Population 10)))
```
#### Note
1. Carbon Footprint does not need to reach the specified amount for this function to succeed.

#### Reasoning
1. This template reflects the labor intensive process of forestation.

#### Source
1. http://urbanforestrynetwork.org/benefits/air%20quality.htm

### Military Resource Creation Template
```
(PRODUCTION ?C
            (INPUTS (Population 10)
                    (Water 10)
                    (Crop 10)
                    (Meat 5)
                    (Electronics 5)
                    (PotentialFossilEnergyUsable 20))
            (OUTPUTS (CarbonFootprint 40)
                     (PopulationWaste 10)
                     (Water 0)
                     (Meat 0)
                     (Crop 0)
                     (PotentialFossilEnergyUsable 0)
                     (Population 0)
                     (Military 1)))
```

### Military Resource Reversion Template
```
(PRODUCTION ?C
            (INPUTS (Military 1)
                    (Water 0)
                    (Meat 0)
                    (Crop 0)
                    (PotentialFossilEnergyUsable 0)
                    (Population 0))
            (OUTPUTS (Population 10)
                     (Water 10)
                     (Crop 10)
                     (Meat 5)
                     (Electronics 5)
                     (PotentialFossilEnergyUsable 20)))
```

## Out-of-scope Recurring Templates

##### Note:
Since reproduction, death, and other recurring changes to a country's state does not to be considered for Part 1, we remove these templates from Part 1.

### Reproduction Template
```
(PRODUCTION ?C
            (INPUTS (Population 2)
                    (Housing 1))
            (OUTPUTS (Housing 1)
                     (Population 3)))
```
#### Reasoning
1. The resource consumption of reproduction is excluded from the current template since it might be included in a separate recurring PRODUCTION function.


### Death Template
```
(PRODUCTION ?C
            (INPUTS (Population 1))
            (OUTPUTS (Population 0)))
```

### Food Consumption Template
```
(PRODUCTION ?C
            (INPUTS (Population 1)
                    (Water 0.7)
                    (Crop 0.2)
                    (Meat 0.07)
                    (PotentialFossilEnergyUsable 6)
                    (PotentialRenewableEnergyUsable 2))
            (OUTPUTS (CarbonFootprint 4)
                     (PopulationWaste 1)
                     (Water 0.7)
                     (Meat 0)
                     (Crop 0)
                     (PotentialFossilEnergyUsable 0)
                     (PotentialRenewableEnergyUsable 0)
                     (Population 1)))
```
#### Note
1. This consumption template is based on the average human yearly consumption. Adjust reoccurrence frequency / quantity as needed.
1. Average person drinks 182.5 gallons of water per year. 182.5 gallon = 0.7 tons = 0.7 unit
1. Recommended consumption for fruit, vegetables, and grain is 6 cups, which is 2190 cups per year, which is about 0.2 unit of crop.
1. Recommended consumption for meat is 6 oz, which is 2190 oz per year, which is about 0.07 unit of meat.
1. Average amount of waste produced per person per year is about 2072 pounds, which is about 1 ton.
1. Global average of carbon footprint per person is about 4 tons.

#### Source
1. https://watertalks.csusb.edu/how-much-water-do-people-use#:~:text=The%20average%20person%20drinks%208,and%20182.5%20gallons%20per%20year.
1. https://ourworldindata.org/grapher/vegetable-consumption-per-capita?tab=chart&country=~USA&region=NorthAmerica
1. https://www.webmd.com/diet/ss/slideshow-serving-sizes
1. https://www.titlemax.com/discovery-center/lifestyle/trash-one-person-produces-year/
1. https://www.nature.org/en-us/get-involved/how-to-help/carbon-footprint-calculator/#:~:text=A%20carbon%20footprint%20is%20the,is%20closer%20to%204%20tons.



## Additional considerations
1. Model water as a renewable resource that only becomes available after certain # of cycles.
1. Model vegetable and meat production as recurring events
