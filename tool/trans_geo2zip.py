# return [zipcode, 4-neighbor zip area]
# find neariest zip-code by zip-center long/lat database
def trans_geo2zip(lat, long, searchTreash=1):
    tozipData = pd.read_csv('data\\zip_code_database_clean.csv')
    #subData = tozipData
    subData = tozipData.loc[tozipData['longitude']>=long-searchTreash]
    subData = tozipData.loc[tozipData['longitude']<=long+searchTreash]
    subData = tozipData.loc[tozipData['latitude']>=lat-searchTreash]
    subData = tozipData.loc[tozipData['latitude']<=lat+searchTreash]
    dis=[]
    for index, row in subData.iterrows():
        distance = (row['longitude']-long)**2+(row['latitude']-lat)**2
        dis.append([row['zip'],distance])
    dis.sort(key=lambda x:x[1])
    #
    ret = dis[:5]
    return ret;
trans_geo2zip(41.11,-74.08)
