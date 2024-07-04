# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 17:01:15 2024

@author: QGW
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cmaps

## 读取数据&画图
ds = Dataset('D:/pythonProject/MPAS/x1.10242.static_latlon_240km.nc').variables
all_vars = ds.keys()   #获取所有变量名称
hgt=np.array(ds['ter'])
lsm=np.array(ds['landmask'])
lon=np.array(ds['longitude'])
lat=np.array(ds['latitude'])
# 使用landmask变量将海洋区域（landmask值为0的区域）设置为NaN
hgt_white = np.where(lsm == 1, hgt, np.nan)
cmap=cmaps.MPL_terrain


#########   plot    ##########################

fig=plt.figure(figsize=(8,8), dpi=300)
ax = plt.axes(projection=ccrs.PlateCarree())
contour=ax.contourf(lon,lat,hgt_white,transform=ccrs.PlateCarree(),cmap=cmap,levels=np.arange(0,5000+100,100))
ax.add_feature(cfeature.COASTLINE, linewidth=1.5)
# 采用绘制经纬度线的方法为Labmert投影地图增加经纬度刻度
ax.gridlines(draw_labels=True,
                linewidth=1,
                color='gray',
                alpha=0.5,
                linestyle='--',
                x_inline=False,
                y_inline=False)

# 在figure下方添加colorbar
l=0.15
b=0.25
w=0.7
h=0.03
rect=[l,b,w,h]
cbar_ax=fig.add_axes(rect)
cbar=plt.colorbar(contour,cax=cbar_ax,orientation='horizontal')
cbar.set_label('Terrain Height (m)',fontsize=13.5)

pic_name = "D:/pythonProject/MPAS/Terrain Height.png" 
plt.show()
fig.savefig(pic_name, bbox_inches='tight', dpi=300)
