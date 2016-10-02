# Windows系统 Visual Studio软件 搭建 PCL 开发环境  --- Ongoing --- 2016年9月30日 星期五

我的电脑系统：**Windows 10 64位系统**
我的 **Visual Studio** 软件：**Visual Studio 2010** 
PCL 版本：**PCL 1.6.0 All-In-One** 

---

## 一 . 下载 PCL


到这个网站下载**PCL-All-In-One Installer**：http://pointclouds.org/downloads/windows.html

![Alt text](https://app.yinxiang.com/shard/s53/res/d93feb38-8101-4b99-b285-22f7dca39908)

> 我也不知道是使用MSVC 2010的32bit 还是64bit的。我就下载使用32位的。
> 我要安装32位还是64位的PCL和相关库包了。这个问题取决于你使用你使用的VS2010是多少位的，而不是你的电脑。我使用的VS2010是32位的。所以我们需要安装PCL是32位：

下载完成：

![Alt text](https://app.yinxiang.com/shard/s53/res/6a01f831-7d10-45f5-8432-03cb7bfeccb9)


---

## 二 . 开始安装 PCL

双击启动刚刚下载的 **PCL-1.6.0-AllnOne-msvc2010-win32.exe** 文件，开始安装：（傻瓜式安装）

![Alt text](https://app.yinxiang.com/shard/s53/res/1f0db3f9-f068-4784-8cf6-9509698710bb)

![Alt text](https://app.yinxiang.com/shard/s53/res/61df3a96-0a71-449f-952d-da6b294be670)

![Alt text](https://app.yinxiang.com/shard/s53/res/d6ae5c20-56e4-4e3b-ab3c-c80acec89859)

![Alt text](https://app.yinxiang.com/shard/s53/res/f38d1096-0380-4403-a539-d81bc596bc97)

选择： 给所有的用户添加环境变量

![Alt text](https://app.yinxiang.com/shard/s53/res/85cae056-707c-4f66-91cb-9536018423c3)

选择一个安装路径：

![Alt text](https://app.yinxiang.com/shard/s53/res/7133a201-03e4-4ab1-bf26-6626e210e7ad)

![Alt text](https://app.yinxiang.com/shard/s53/res/2f08130e-d47e-4fc2-b6be-0256abbaf3dd)

![Alt text](https://app.yinxiang.com/shard/s53/res/8b2016f3-d736-413d-95bf-40e776e4f7b3)

![Alt text](https://app.yinxiang.com/shard/s53/res/60705794-fa5b-4a13-992d-75c4ecd0cdea)


安装完PCL，会自动安装OpenNI库：

![Alt text](https://app.yinxiang.com/shard/s53/res/661933ff-4e3b-4286-a0d0-a966fbbc2bd1)


![Alt text](https://app.yinxiang.com/shard/s53/res/291ca04b-bd64-45ea-b289-e271adb258f9)

出现问题（正常，后面我们会解决这个问题。）
![Alt text](https://app.yinxiang.com/shard/s53/res/f5eef31c-704d-4fd4-9e73-093dac8e51b4)

OpenNI 没有安装成功

![Alt text](https://app.yinxiang.com/shard/s53/res/254cba9c-3ac4-47e7-9d09-2bee18af4e7d)

提示：
![Alt text](https://app.yinxiang.com/shard/s53/res/525557dd-832f-49ae-a7e8-5f8ae7282b7f)

**OpenNI**没有安装成功，就导致了后面自动安装**PrimeSense Sensor KinectModPCL**库，也没有成功。

![Alt text](https://app.yinxiang.com/shard/s53/res/5ef65e67-ae43-4d81-b17d-43894866a9e0)

最后提示：

![Alt text](https://app.yinxiang.com/shard/s53/res/f19546d3-4c20-4202-87af-4805949b86cc)

完成：

![Alt text](https://app.yinxiang.com/shard/s53/res/4740a330-4d07-4574-95f9-e5b8e683d816)


**这样的结果就是：**
PCL 安装成功了，但是环境变量没有添加成功。**OpenNI** 和  **PrimeSense Sensor KinectModPCL** 这两个都没有安装成功。

---

## 单独安装 **OpenNI** 和  **PrimeSense Sensor KinectModPCL** 这两个软件包

到这里：http://pan.baidu.com/s/1o8B6tM6 下载 **OpenNI** 和  **PrimeSense Sensor KinectModPCL** 这两个软件包。

![Alt text](https://app.yinxiang.com/shard/s53/res/9688a7d9-ae72-4a63-9ebf-d21ec94bd973)


双击 **OpenNI** 软件安装包，进行安装。

![Alt text](https://app.yinxiang.com/shard/s53/res/2e27cc1b-eb31-4221-9d41-0dbab87270e4)

![Alt text](https://app.yinxiang.com/shard/s53/res/6070bba3-5c85-4a53-baf9-099294e7b277)

![Alt text](https://app.yinxiang.com/shard/s53/res/ada4fc63-e57a-44e2-9afa-43a49826fb46)

![Alt text](https://app.yinxiang.com/shard/s53/res/ef0b7c0c-b0e6-466d-8bf5-bd49b57edcb2)

![Alt text](https://app.yinxiang.com/shard/s53/res/16698d93-46d3-414e-a5c4-2564b6b46ed7)

**OpenNI** 软件包安装完成。


---

双击 **PrimeSense Sensor KinectModPCL** 软件包，进行安装。

![Alt text](https://app.yinxiang.com/shard/s53/res/f877a439-9a7c-4960-b58a-0be4bc813ef8)

![Alt text](https://app.yinxiang.com/shard/s53/res/aa2ae655-09bf-4d26-bb0b-000f42a39177)

![Alt text](https://app.yinxiang.com/shard/s53/res/70c665fe-a2e5-4bc6-8d67-6f3273116da3)

![Alt text](https://app.yinxiang.com/shard/s53/res/d8c87f5f-ade9-4c90-8d36-925740c5a831)

![Alt text](https://app.yinxiang.com/shard/s53/res/184effac-02ef-4eff-8dac-1f3089294dd3)

**PrimeSense Sensor KinectModPCL** 软件包安装完成。

## 配置环境变量

打开 **环境变量** 窗口：

![Alt text](https://app.yinxiang.com/shard/s53/res/c453328f-6f9e-43c0-b6ee-8127f7eb4496)

![Alt text](https://app.yinxiang.com/shard/s53/res/0a71a7f1-d63b-4441-92f3-4eeeea6a5157)

![Alt text](https://app.yinxiang.com/shard/s53/res/bcf2bc74-a472-4f7b-8a1c-2961f5bd68be)

![Alt text](https://app.yinxiang.com/shard/s53/res/9d832640-43bc-4bbb-94f6-fbdaa5947a8a)

![Alt text](https://app.yinxiang.com/shard/s53/res/17dc389a-8fcd-4153-970b-fda42b63e92b)

![Alt text](https://app.yinxiang.com/shard/s53/res/cde1e005-4b2a-4e5a-98d2-9c5c63606404)

需要在 **系统变量** 里面添加下面的 环境变量：

在**系统变量**中新建一个变量：`PCL_ROOT`，并在里面添加：`C:\third_packages\PCL 1.6.0`。如下图所示：

![Alt text](https://app.yinxiang.com/shard/s53/res/222b57a1-299b-4457-a619-4c8f61fb5361)

双击 **系统变量** 里面的 `Path` 。

![Alt text](https://app.yinxiang.com/shard/s53/res/87e43023-a9c2-4b7a-8bd4-9b8530827cba)

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

![Alt text](https://app.yinxiang.com/shard/s53/res/f3ae2320-16c3-4bb9-b150-727bffa0d756)

现在，环境变量而配置完成了。

---

## 三 . 开始为 **Visual Studio 2010** 软件搭建 PCL 开发环境

启动 **Visual Studio 2010 ** 软件。

新建一个 **Win32 控制台应用程序** 工程：

![Alt text](https://app.yinxiang.com/shard/s53/res/92696587-6756-4aab-9dd5-11fa36efbeeb)

在工程里面新添加一个 `main.cpp` 文件。

在 **属性管理器** 里面，选择： **工程名** -> **Debug | Win32** -> **Microsoft.Cpp.Win32.user**

![Alt text](https://app.yinxiang.com/shard/s53/res/84fca302-2fb8-458a-82df-133d80f529d2)

配置 **包含目录** ：

![Alt text](https://app.yinxiang.com/shard/s53/res/44f068a0-2898-49ae-884f-1da2d9fed458)

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

![Alt text](https://app.yinxiang.com/shard/s53/res/bb154666-c8ba-45b5-80b6-d6af2890ada8)

---

配置 **库目录**：

![Alt text](https://app.yinxiang.com/shard/s53/res/04fcf619-a0aa-42d4-ae5e-b023f366edde)

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


![Alt text](https://app.yinxiang.com/shard/s53/res/bb2013fe-e979-4045-ae01-4ab3b758c5f4)

---

配置 **附加依赖项**：

![Alt text](https://app.yinxiang.com/shard/s53/res/282f62cd-d2ab-4bf3-899a-e30369bd1ba2)

![Alt text](https://app.yinxiang.com/shard/s53/res/3f2e3f0f-9c15-47ed-917a-37ac92b3ca69)

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

![Alt text](https://app.yinxiang.com/shard/s53/res/b59bc5dd-8d7c-45e7-b288-7b4a9a870de1)


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

![Alt text](https://app.yinxiang.com/shard/s53/res/57faa3f7-a558-40dd-bf93-f688c808b401)


---

# 搞定

---

**总结：**
本教程适用于 **Windows** 系列的操作系统，不光光适用于 **Windows 10**。还有，在安装时遇到错误时正常的。因为**PCL ** 这个库已经被 **ROS** 收购了，现在不在单独维护了。如果你想安装 **PCL** 最新的版本，你需要到 **GitHub** 上下载最新的 **PCL** 源代码，然后自己手动编译。


