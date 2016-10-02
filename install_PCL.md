# Windows系统 Visual Studio软件 搭建 PCL 开发环境  --- Ongoing --- 2016年9月30日 星期五

我的电脑系统：**Windows 10 64位系统**
我的 **Visual Studio** 软件：**Visual Studio 2010** 
PCL 版本：**PCL 1.6.0 All-In-One** 

---

## 一 . 下载 PCL


到这个网站下载**PCL-All-In-One Installer**：http://pointclouds.org/downloads/windows.html

![Alt text](./1475185523275.png)

> 我也不知道是使用MSVC 2010的32bit 还是64bit的。我就下载使用32位的。
> 我要安装32位还是64位的PCL和相关库包了。这个问题取决于你使用你使用的VS2010是多少位的，而不是你的电脑。我使用的VS2010是32位的。所以我们需要安装PCL是32位：

下载完成：

![Alt text](./1475185542021.png)


---

## 二 . 开始安装 PCL

双击启动刚刚下载的 **PCL-1.6.0-AllnOne-msvc2010-win32.exe** 文件，开始安装：（傻瓜式安装）

![Alt text](./1475291577407.png)

![Alt text](./1475291600927.png)

![Alt text](./1475185222317.png)

![Alt text](./1475185231949.png)

选择： 给所有的用户添加环境变量

![Alt text](./1475185283732.png)

选择一个安装路径：

![Alt text](./1475185320213.png)

![Alt text](./1475185329838.png)

![Alt text](./1475185345044.png)

![Alt text](./1475185362285.png)


安装完PCL，会自动安装OpenNI库：

![Alt text](./1475185575424.png)


![Alt text](./1475185603401.png)

出现问题（正常，后面我们会解决这个问题。）
![Alt text](./1475185629454.png)

OpenNI 没有安装成功

![Alt text](./1475185647731.png)

提示：
![Alt text](./1475185665678.png)

**OpenNI**没有安装成功，就导致了后面自动安装**PrimeSense Sensor KinectModPCL**库，也没有成功。

![Alt text](./1475185706676.png)

最后提示：

![Alt text](./1475185716353.png)

完成：

![Alt text](./1475185727627.png)


**这样的结果就是：**
PCL 安装成功了，但是环境变量没有添加成功。**OpenNI** 和  **PrimeSense Sensor KinectModPCL** 这两个都没有安装成功。

---

## 单独安装 **OpenNI** 和  **PrimeSense Sensor KinectModPCL** 这两个软件包

到这里：http://pan.baidu.com/s/1o8B6tM6 下载 **OpenNI** 和  **PrimeSense Sensor KinectModPCL** 这两个软件包。

![Alt text](./1475377441456.png)


双击 **OpenNI** 软件安装包，进行安装。

![Alt text](./1475367780708.png)

![Alt text](./1475367560285.png)

![Alt text](./1475367476818.png)

![Alt text](./1475367524926.png)

![Alt text](./1475367579623.png)

**OpenNI** 软件包安装完成。


---

双击 **PrimeSense Sensor KinectModPCL** 软件包，进行安装。

![Alt text](./1475367635844.png)

![Alt text](./1475367677922.png)

![Alt text](./1475367689929.png)

![Alt text](./1475367700740.png)

![Alt text](./1475367714701.png)

**PrimeSense Sensor KinectModPCL** 软件包安装完成。

## 配置环境变量

打开 **环境变量** 窗口：

![Alt text](./1475367924551.png)

![Alt text](./1475367940872.png)

![Alt text](./1475367956501.png)

![Alt text](./1475367975994.png)

![Alt text](./1475367995536.png)

![Alt text](./1475368008355.png)

需要在 **系统变量** 里面添加下面的 环境变量：

在**系统变量**中新建一个变量：`PCL_ROOT`，并在里面添加：`C:\third_packages\PCL 1.6.0`。如下图所示：

![Alt text](./1475368259155.png)

双击 **系统变量** 里面的 `Path` 。

![Alt text](./1475368345129.png)

在里面添加下面的这些环境变量：

```
C:\third_packages\OpenNI\Bin
%PCL_ROOT%\bin
%PCL_ROOT%\3rdParty\FLANN\bin
%PCL_ROOT%\3rdParty\Qhull\bin
%PCL_ROOT%\3rdParty\Eigen\bin
%PCL_ROOT%\3rdParty\VTK\bin
C:\third_packages\PrimeSense\SensorKinect\Bin
```

添加完成后，如下图所示：

![Alt text](./1475368538662.png)

现在，环境变量而配置完成了。

---

## 三 . 开始为 **Visual Studio 2010** 软件搭建 PCL 开发环境

启动 **Visual Studio 2010 ** 软件。

新建一个 **Win32 控制台应用程序** 工程：

![Alt text](./1475368854869.png)

在工程里面新添加一个 `main.cpp` 文件。

在 **属性管理器** 里面，选择： **工程名** -> **Debug | Win32** -> **Microsoft.Cpp.Win32.user**

![Alt text](./1475368971651.png)

配置 **包含目录** ：

![Alt text](./1475369096790.png)

将下面的路径一个一个的添加进去：

```
C:\third_packages\OpenNI\Include\Win32
C:\third_packages\OpenNI\Include
C:\third_packages\PCL 1.6.0\3rdParty\VTK\include\vtk-5.8
C:\third_packages\PCL 1.6.0\3rdParty\Qhull\include
C:\third_packages\PCL 1.6.0\3rdParty\FLANN\include
C:\third_packages\PCL 1.6.0\3rdParty\Eigen\include
C:\third_packages\PCL 1.6.0\3rdParty\Boost\include
C:\third_packages\PCL 1.6.0\include\pcl-1.6
```

添加完毕之后，如下图：

![Alt text](./1475369183703.png)

---

配置 **库目录**：

![Alt text](./1475375755202.png)

将下面的路径一个一个的添加进去：

```
C:\third_packages\OpenNI\Lib
C:\third_packages\PCL 1.6.0\3rdParty\VTK\lib\vtk-5.8
C:\third_packages\PCL 1.6.0\3rdParty\Qhull\lib
C:\third_packages\PCL 1.6.0\3rdParty\FLANN\lib
C:\third_packages\PCL 1.6.0\3rdParty\Boost\lib
C:\third_packages\PCL 1.6.0\lib
```

添加完毕之后，如下图：


![Alt text](./1475375887964.png)

---

配置 **附加依赖项**：

![Alt text](./1475376218630.png)

![Alt text](./1475376272894.png)

添加下面的内容：

```
opengl32.lib
pcl_apps_debug.lib
pcl_kdtree_debug.lib
pcl_keypoints_debug.lib
pcl_io_debug.lib
pcl_io_ply_debug.lib
pcl_octree_debug.lib
pcl_registration_debug.lib
pcl_surface_debug.lib
pcl_search_debug.lib
pcl_segmentation_debug.lib
pcl_features_debug.lib
pcl_filters_debug.lib
pcl_tracking_debug.lib
pcl_visualization_debug.lib
pcl_common_debug.lib
pcl_sample_consensus_debug.lib
flann_cpp_s-gd.lib
flann_cuda_s-gd.lib
flann-gd.lib
flann_s-gd.lib
qhull6_d.lib
qhullcpp_d.lib
qhullstatic_d.lib
qhullstatic_p_d.lib
libboost_system-vc100-mt-gd-1_47.lib
libboost_filesystem-vc100-mt-gd-1_47.lib
libboost_thread-vc100-mt-gd-1_47.lib
libboost_date_time-vc100-mt-gd-1_47.lib
libboost_iostreams-vc100-mt-gd-1_47.lib
vtkalglib-gd.lib
vtkCharts-gd.lib
vtkCommon-gd.lib
vtkDICOMParser-gd.lib
vtkexoIIc-gd.lib
vtkexpat-gd.lib
vtkFiltering-gd.lib
vtkfreetype-gd.lib
vtkftgl-gd.lib
vtkGenericFiltering-gd.lib
vtkGeovis-gd.lib
vtkGraphics-gd.lib
vtkhdf5-gd.lib
vtkHybrid-gd.lib
vtkImaging-gd.lib
vtkInfovis-gd.lib
vtkIO-gd.lib
vtkjpeg-gd.lib
vtklibxml2-gd.lib
vtkmetaio-gd.lib
vtkNetCDF-gd.lib
vtkNetCDF_cxx-gd.lib
vtkpng-gd.lib
vtkproj4-gd.lib
vtkRendering-gd.lib
vtksqlite-gd.lib
vtksys-gd.lib
vtktiff-gd.lib
vtkverdict-gd.lib
vtkViews-gd.lib
vtkVolumeRendering-gd.lib
vtkWidgets-gd.lib
vtkzlib-gd.lib
QVTK-gd.lib
openNI.lib
```

添加完之后，如下图所示：

![Alt text](./1475376317656.png)


# 完成

完成 Windows系统 Visual Studio软件 搭建 PCL 开发环境。接下来，我们测试环境是否可以使用。

---

## 四 . 测试刚刚搭建好的**Visual Studio 2010** 软件 的PCL 开发环境


我们将下面的测试代码复制粘贴到 `main.cpp` 文件里。这段代码是来着这个网站：http://pointclouds.org/documentation/tutorials/cloud_viewer.php#cloud-viewer

```cpp
#include <pcl/visualization/cloud_viewer.h>
#include <iostream>
#include <pcl/io/io.h>
#include <pcl/io/pcd_io.h>
    
int user_data;
    
void 
viewerOneOff (pcl::visualization::PCLVisualizer& viewer)
{
    viewer.setBackgroundColor (1.0, 0.5, 1.0);
    pcl::PointXYZ o;
    o.x = 1.0;
    o.y = 0;
    o.z = 0;
    viewer.addSphere (o, 0.25, "sphere", 0);
    std::cout << "i only run once" << std::endl;
    
}
    
void 
viewerPsycho (pcl::visualization::PCLVisualizer& viewer)
{
    static unsigned count = 0;
    std::stringstream ss;
    ss << "Once per viewer loop: " << count++;
    viewer.removeShape ("text", 0);
    viewer.addText (ss.str(), 200, 300, "text", 0);
    
    //FIXME: possible race condition here:
    user_data++;
}
    
int 
main ()
{
    pcl::PointCloud<pcl::PointXYZRGBA>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZRGBA>);
    pcl::io::loadPCDFile ("my_point_cloud.pcd", *cloud);
    
    pcl::visualization::CloudViewer viewer("Cloud Viewer");
    
    //blocks until the cloud is actually rendered
    viewer.showCloud(cloud);
    
    //use the following functions to get access to the underlying more advanced/powerful
    //PCLVisualizer
    
    //This will only get called once
    viewer.runOnVisualizationThreadOnce (viewerOneOff);
    
    //This will get called once per visualization iteration
    viewer.runOnVisualizationThread (viewerPsycho);
    while (!viewer.wasStopped ())
    {
    //you can also do cool processing here
    //FIXME: Note that this is running in a separate thread from viewerPsycho
    //and you should guard against race conditions yourself...
    user_data++;
    }
    return 0;
}
```

到这个网站，下载一个`pcl` 文件。https://github.com/PointCloudLibrary/pcl/blob/master/test/five_people.pcd

将这个文件放到与`main.cpp` 文件同一个路径下。

接着将上面代码中`main()` 函数中的下面这端代码：
```cpp
    pcl::io::loadPCDFile ("my_point_cloud.pcd", *cloud);
```
修改为：
```cpp
    pcl::io::loadPCDFile ("five_people.pcd", *cloud);
```

运行程序：

![Alt text](./1475377190789.png)


---

# 搞定

---

**总结：**
本教程适用于 **Windows** 系列的操作系统，不光光适用于 **Windows 10**。还有，在安装时遇到错误时正常的。因为**PCL ** 这个库已经被 **ROS** 收购了，现在不在单独维护了。如果你想安装 **PCL** 最新的版本，你需要到 **GitHub** 上下载最新的 **PCL** 源代码，然后自己手动编译。


