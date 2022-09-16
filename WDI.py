import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import math

data = pd.read_csv('Indicators.csv')

count_plots = 10
countryCodes = data['CountryCode'].unique()
countryName = data['CountryName'].unique()
co2_indicator = 'CO2 emissions \(metric'
int_migrant = 'International migrant stock, total'
total_pop = 'Population, total'
gdp_capita = 'GDP per capita \(constant 2005'
int_migrant_percent = 'International migrant stock \(\% of population\)'
renewable_energy = 'Electricity production from renewable sources'
electric_power_consumption = 'Electric power consumption \(kWh per capita\)'

urban_population_percent = 'Urban population \(\% of total\)'
net_income_from_abroad =  'Net income from abroad \(current US\$\)'

fossil_fuel_energy_consumption_percent = 'Fossil fuel energy consumption \(\% of total\)'
export_goods_service_percent = 'Exports of goods and services \(\% of GDP\)'
merchandise_trade_percent = 'Merchandise trade \(\% of GDP\)'

hist_country = countryCodes
fig, axs = plt.subplots(count_plots, figsize=(10,count_plots*10))
co2_inidcator_mask = data['IndicatorName'].str.contains(co2_indicator)     
mask3 = data['IndicatorName'].str.contains(int_migrant)
mask4 = data['IndicatorName'].str.contains(total_pop)
gdp_capita_mask = data['IndicatorName'].str.contains(gdp_capita)
int_migrant_percent_mask = data['IndicatorName'].str.contains(int_migrant_percent)

fossil_fuel_energy_consumption_percent_mask = data['IndicatorName'].str.contains(fossil_fuel_energy_consumption_percent)
export_goods_service_percent_mask = data['IndicatorName'].str.contains(export_goods_service_percent)

electric_power_consumption_mask = data['IndicatorName'].str.contains(electric_power_consumption)
urban_population_percent_mask = data['IndicatorName'].str.contains(urban_population_percent)

merchandise_trade_percent_mask = data['IndicatorName'].str.contains(merchandise_trade_percent)

renewable_energy_mask = data['IndicatorName'].str.contains(renewable_energy)
net_income_from_abroad_mask = data['IndicatorName'].str.contains(net_income_from_abroad)


co2_data = data[co2_inidcator_mask] 
co2_data_sample = co2_data.sort_values(by = ['Value', 'Year'], ascending = False)
co2_data_sample_subset = co2_data_sample.head(30)
#print(x1)

stage6 = data[gdp_capita_mask] 
y = stage6.sort_values(by = ['Value', 'Year'], ascending = False)
y1 = y.head(60)

most_gdp_countries_code = y1[['CountryName', 'CountryCode']].groupby('CountryCode').count()
most_gdp_countries_code = most_gdp_countries_code.index

most_gdp_countries_name = y1[['CountryName', 'CountryCode']].groupby('CountryName').count()
most_gdp_countries_name = most_gdp_countries_name.index

most_polutant_count_name = co2_data_sample_subset[['CountryName','CountryCode']].groupby('CountryName').count()
most_polutant_count_name = most_polutant_count_name.index

axs[0].axis([1975, 2015,0,70])
axs[1].axis([1975, 2015,20000,100000])
axs[2].axis([1975, 2015,0,5000000])
axs[3].axis([1975, 2015,0,100])
axs[4].axis([1975, 2015,math.pow(10, 5),math.pow(10, 9)])
#axs[5].axis([1975, 2015,math.pow(10, 3),7*math.pow(10, 4)])
#axs[5].axis([1975, 2015]) doesn't work


countryCodes_custom = []

for i in range(len(most_gdp_countries_code)):
    #if (most_gdp_countries_code[i] == 'LIE' or most_gdp_countries_code[i] == 'MCO'):
    #    continue
    countryCodes_custom.append(most_gdp_countries_code[i])
    
    
#most_polutant_count = x1[['CountryName','Value']].groupby('Value').count().sort_values(by = ['Value'], ascending = False)

#highest_gdp_count = y1[['CountryName','Value']].groupby('CountryName').count().sort_values(by = ['Value'], ascending = False)
#highest_gdp_count

for i in range(len(countryCodes_custom)):
    country_code_mask = data['CountryCode'].str.contains(countryCodes_custom[i])

    co2_data_per_country = data[co2_inidcator_mask & country_code_mask]
    stage2 = data[country_code_mask & mask3]
#    stage3 = data[mask2 & mask4]
    gdp_data_per_country = data[country_code_mask & gdp_capita_mask]
    int_migrant_percent_per_country = data[country_code_mask & int_migrant_percent_mask]
    renewable_energy_per_country = data[country_code_mask & renewable_energy_mask]
    renewable_energy_per_country = renewable_energy_per_country[['CountryName', 'Value', 'Year']].groupby(['Year', 'CountryName'], as_index=False).sum()
    urban_population_percent_per_country = data[country_code_mask & urban_population_percent_mask]
    electric_power_consumption_per_country = data[country_code_mask & electric_power_consumption_mask]
    net_income_from_abroad_per_country = data[country_code_mask & net_income_from_abroad_mask]
    merchandise_trade_percent_per_country = data[country_code_mask & merchandise_trade_percent_mask]
    
    fossil_fuel_energy_consumption_percent_per_country = data[country_code_mask & fossil_fuel_energy_consumption_percent_mask]
    export_goods_service_percent_per_country = data[country_code_mask & export_goods_service_percent_mask]
        
    if (co2_data_per_country.shape[0] > 1):
        axs[0].plot(co2_data_per_country['Year'].values, co2_data_per_country['Value'].values, label = co2_data_per_country['CountryName'].unique() +  ' ' + 'CO2 emissions (metric tons per capita)')
        min_year_co2 = co2_data_per_country['Year'].min()
        max_year_co2 = co2_data_per_country['Year'].max()
    if (gdp_data_per_country.shape[0] > 1):
        min_year_gdp = gdp_data_per_country['Year'].min()
        max_year_gdp = gdp_data_per_country['Year'].max()
    if (co2_data_per_country.shape[0] > 1 and gdp_data_per_country.shape[0] > 1):
        min_year_co2_gdp = max(min_year_gdp, min_year_co2)
        max_year_co2_gdp = min(max_year_gdp, max_year_co2)
        co2_data_for_gdp_per_country_corrcoef = co2_data_per_country[co2_data_per_country['Year'] <= max_year_co2_gdp]
        gdp_data_for_co2_per_country_corrcoef = gdp_data_per_country[gdp_data_per_country['Year'] <= max_year_co2_gdp]
        co2_data_for_gdp_per_country_corrcoef = co2_data_for_gdp_per_country_corrcoef[co2_data_for_gdp_per_country_corrcoef['Year'] >= min_year_co2_gdp]
        gdp_data_for_co2_per_country_corrcoef = gdp_data_for_co2_per_country_corrcoef[gdp_data_for_co2_per_country_corrcoef['Year'] >= min_year_co2_gdp]
    
    if (merchandise_trade_percent_per_country.shape[0] > 1):
        axs[9].plot(merchandise_trade_percent_per_country['Year'].values, merchandise_trade_percent_per_country['Value'].values, label = merchandise_trade_percent_per_country['CountryName'].unique()+ ' Merchandise %')
    if (export_goods_service_percent_per_country.shape[0] > 1):
        axs[8].plot(export_goods_service_percent_per_country['Year'].values, export_goods_service_percent_per_country['Value'].values, label = export_goods_service_percent_per_country['CountryName'].unique()+ ' export of goods and service %')  
    if (renewable_energy_per_country.shape[0] > 1):
        axs[4].plot(renewable_energy_per_country['Year'].values, renewable_energy_per_country['Value'].values, label = renewable_energy_per_country['CountryName'].unique()+ ' Electricity production from renewable sources')
    if (fossil_fuel_energy_consumption_percent_per_country.shape[0] > 1):
        axs[7].plot(fossil_fuel_energy_consumption_percent_per_country['Year'].values, fossil_fuel_energy_consumption_percent_per_country['Value'].values, label = fossil_fuel_energy_consumption_percent_per_country['CountryName'].unique()+ ' fossil fuel energy consumption percent')  
    if (electric_power_consumption_per_country.shape[0] > 1):
        electric_power_consumption_corrcoef = electric_power_consumption_per_country[electric_power_consumption_per_country['Year']< 2012]
        electric_power_consumption_corrcoef = electric_power_consumption_corrcoef[electric_power_consumption_corrcoef['Year'] >1974]  
        #print ('correlation coefficient for electric_power_consumption and gdp')
        #print(np.corrcoef(electric_power_consumption_corrcoef['Value'],gdp_data_per_country_corrcoef['Value']))
        axs[5].plot(electric_power_consumption_per_country['Year'].values, electric_power_consumption_per_country['Value'].values, label = electric_power_consumption_per_country['CountryName'].unique()+ ' Electricity consumption')

        
    if (co2_data_for_gdp_per_country_corrcoef.shape[0] > 1 and gdp_data_for_co2_per_country_corrcoef.shape[0] > 1):
        print ('correlation coefficient for CO2 and GDP for ' + countryCodes_custom[i])
        print(np.corrcoef(co2_data_for_gdp_per_country_corrcoef['Value'],gdp_data_for_co2_per_country_corrcoef['Value']))
        
    #this snippet does not work becuase migrant data is collected once every 5 years in this dataset    
    #min_int_migrant_per_country = int_migrant_percent_per_country['Year'].min()
    #max_int_migrant_per_country = int_migrant_percent_per_country['Year'].max()
    
    #min_year_migrant_gdp = max(min_year_gdp, min_int_migrant_per_country)
    #max_year_migrant_gdp = min(max_year_gdp, max_int_migrant_per_country)
    
    
    #gdp_data_for_migrant_per_country_corrcoef = gdp_data_per_country[gdp_data_per_country['Year'] <= max_year_migrant_gdp]
    #int_migrant_data_for_gdp_per_country_corrcoef = int_migrant_percent_per_country[int_migrant_percent_per_country['Year'] <= max_year_migrant_gdp]
    #gdp_data_for_migrant_per_country_corrcoef = gdp_data_for_migrant_per_country_corrcoef[gdp_data_for_migrant_per_country_corrcoef['Year'] >= min_year_migrant_gdp]
    #int_migrant_data_for_gdp_per_country_corrcoef = int_migrant_data_for_gdp_per_country_corrcoef[int_migrant_data_for_gdp_per_country_corrcoef['Year'] >= min_year_migrant_gdp]
    
    #if (gdp_data_for_migrant_per_country_corrcoef.shape[0] != 0 and int_migrant_data_for_gdp_per_country_corrcoef.shape[0] != 0):
    #    print ('----------------------')
    #    print ('correlation coefficient for gdp and migrant percent')
    #    print(np.corrcoef(int_migrant_data_for_gdp_per_country_corrcoef['Value'],gdp_data_for_migrant_per_country_corrcoef['Value']))
    #    print ('----------------------')
    
    
    #this snippet does not work becuase migrant data is collected once every 5 years in this dataset    
    #min_int_migrant_per_country = int_migrant_percent_per_country['Year'].min()
    #max_int_migrant_per_country = int_migrant_percent_per_country['Year'].max()
    
    #min_year_migrant_co2 = max(min_year_co2, min_int_migrant_per_country)
    #max_year_migrant_co2 = min(max_year_co2, max_int_migrant_per_country)
    
    
    #co2_data_for_migrant_per_country_corrcoef = co2_data_per_country[co2_data_per_country['Year'] <= max_year_migrant_co2]
    #int_migrant_data_for_co2_per_country_corrcoef = int_migrant_percent_per_country[int_migrant_percent_per_country['Year'] <= max_year_migrant_co2]
    #co2_data_for_migrant_per_country_corrcoef = co2_data_for_migrant_per_country_corrcoef[co2_data_for_migrant_per_country_corrcoef['Year'] >= min_year_migrant_co2]
    #int_migrant_data_for_co2_per_country_corrcoef = int_migrant_data_for_co2_per_country_corrcoef[int_migrant_data_for_co2_per_country_corrcoef['Year'] >= min_year_migrant_co2]
    
    #if (co2_data_for_migrant_per_country_corrcoef.shape[0] != 0 and int_migrant_data_for_co2_per_country_corrcoef.shape[0] != 0):
    #    print ('----------------------')
    #    print ('correlation coefficient for co2 and migrant percent')
    #    print(np.corrcoef(int_migrant_data_for_co2_per_country_corrcoef['Value'],co2_data_for_migrant_per_country_corrcoef['Value']))
    #    print ('----------------------')
    
    
    gdp_data_and_int_migrant_percent_per_country = gdp_data_per_country.merge(int_migrant_percent_per_country, on='Year', how='inner')
    if (gdp_data_and_int_migrant_percent_per_country.shape[0] > 1):
        print ('correlation coefficient for GDP and migrant percent' + countryCodes_custom[i])
        print(np.corrcoef(gdp_data_and_int_migrant_percent_per_country['Value_x'],gdp_data_and_int_migrant_percent_per_country['Value_y']))
    
    co2_data_and_int_migrant_percent_per_country = co2_data_per_country.merge(int_migrant_percent_per_country, on='Year', how='inner')
    if (co2_data_and_int_migrant_percent_per_country.shape[0] > 1):
        print ('correlation coefficient for CO2 and migrant percent' + countryCodes_custom[i])
        print(np.corrcoef(co2_data_and_int_migrant_percent_per_country['Value_x'],co2_data_and_int_migrant_percent_per_country['Value_y']))
        
    axs[1].plot(gdp_data_per_country['Year'].values, gdp_data_per_country['Value'].values, label = gdp_data_per_country['CountryName'].unique()+ ' GDP Per Capita (US$)')
    axs[2].plot(stage2['Year'].values, stage2['Value'].values, label = stage2['CountryName'].unique()+ ' immigration population total')
    axs[3].plot(int_migrant_percent_per_country['Year'].values, int_migrant_percent_per_country['Value'].values, label = int_migrant_percent_per_country['CountryName'].unique()+ ' immigration population percent')
    axs[6].plot(net_income_from_abroad_per_country['Year'].values, net_income_from_abroad_per_country['Value'].values, label = net_income_from_abroad_per_country['CountryName'].unique()+ ' income from abroad per country')
    #renewable_energy_per_country
    
    #plt.plot(stage2['Year'].values, stage2['Value'].values, label = countryName[i]+ ' % immigration population')
    #plt.plot(stage3['Year'].values, stage3['Value'].values/(math.pow(10, 8)), label = countryName[i]+ ' total population')
    
    # Label the axes
#    plt.xlabel('Year')
#    fig.
#    axs[0].ylabel(stage['IndicatorName'].iloc[0])

#label the figure
    #plt.title('CO2 Emissions in The world')

# to make more honest, start they y axis at 0


#axs[0].xaxis.zoom(-2)
for i in range (len(axs)):
    axs[i].grid()
    axs[i].legend()

plt.show()
#plt.savefig('test.png')