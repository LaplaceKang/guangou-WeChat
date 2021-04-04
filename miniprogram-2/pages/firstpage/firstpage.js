//导入要请求的DjangoURL（可作为全局变量）
import {
  DjangoURL
} from '../../utils/util.js'
//导入场馆运动类型
import {
  Map_CourtType,courtTypeColor
} from '../../utils/typeMap.js'
import Toast from '../../miniprogram/miniprogram_npm/weapp/toast/toast';

Page({
  /**
   * 页面的初始数据
   */
  data: {
    active: 0,
    list: [{
        "url": "/pages/firstpage/firstpage",
        "icon": "wap-home",
        "text": "首页"
      },
      {
        "url": "/pages/orderMeal/orderMeal",
        "icon": "search",
        "text": "课程"
      },
      {
        "url": "/pages/index/index",
        "icon": "manager",
        "text": "我的"
      }
    ],
    imgUrls: [
      "/images/3.jpg",
      "/images/3.jpg",
      "/images/3.jpg"
    ],
    venue: [],
    longitude: 116.346352,
    latitude: 39.970601,
    cityid: 1,
    page: 1,
    left: 0.6048 // 初始化滑块位置
  },
  //获取首页下方推荐的总场馆信息
  getVenue() {
    var that = this
    wx.request({
      url: DjangoURL+'wx/venue/getIndexVenue?cityid=' + that.data.cityid + '&longitude=' + that.data.longitude + '&latitude=' + that.data.latitude + '&page=' + that.data.page,
      method: "GET",
      success: function (res) {
        that.setData({
          venue: that.data.venue.concat(res.data.data),
          showAll: res.data.showAll,
          showLoading: false //隐藏加载中Toast
        })
        console.log(res.data)
        // console.log(res.data.showAll)
      }
    })
  },
  //获取此城市的场馆类型
  getCourtType() {
    var that = this
    wx.request({
      url: DjangoURL+'wx/venue/getCourtType?cityid=' + that.data.cityid,
      method: "GET",
      success: function (res) {
        let courtType=res.data.data
        for(let i=0;i<res.data.data.length;i++){
          //根据courttypeid的值来增加，而不是下标
          courtType[i]['name']=Map_CourtType[courtType[i].courttypeid+''][0]
          courtType[i]['eName']=Map_CourtType[courtType[i].courttypeid+''][1]
        }
        that.setData({
          courttype: courtType
        })
        // console.log(courtType)
      }
    })
  },
  //跳转到筛选总场馆页
  toStadium(event) {
    var that = this
    let index = parseInt(event.currentTarget.dataset.index) //获取点击的运动类型的下标
    wx.navigateTo({ //跳转页面
      url: '/pages/stadium/stadium?courttypeid=' + that.data.courttype[index].courttypeid + '&longitude=' + that.data.longitude + '&latitude=' + that.data.latitude + '&cityid=' + that.data.cityid
    })
  },
  //跳转到场馆详情页
  toCampus(event) {
    var that = this
    let index = parseInt(event.currentTarget.dataset.index) //获取点击的场馆的下标
    console.log(that.data.venue[index].venueid)
    let courttype = JSON.stringify(that.data.venue[index].courttype)
    // console.log(courttype)
    wx.navigateTo({ //跳转页面
      url: '/pages/campus/campus?venueid=' + that.data.venue[index].venueid + '&courttype=' + courttype + '&venuename=' + that.data.venue[index].venuename + '&longitude=' + that.data.venue[index].longitude + '&latitude=' + that.data.venue[index].latitude
    })
  },
  //金刚区滑动事件
  scroll(event) {
    let scrollLeft = event.detail.scrollLeft + 375;
    let scrllWidth = event.detail.scrollWidth;
    let left;
    // console.log(scrllWidth)
    // console.log(scrollLeft)
    if (scrollLeft < 375) {
      left = `0.6048`
    } else {
      left = `${(scrollLeft) / scrllWidth * 100}%`
    }
    // console.log(left)
    this.setData({
      left, //模拟滑块滑动 根据css设置 距离左边的百分比
    })
  },
  //事件处理函数
  toupper: function () {
    console.log("触发了toupper");
  },
  toCourse: function (event) {
    wx.navigateTo({ //跳转页面
      url: '/pages/course/course'
    })
  },
  toMy: function (event) {
    wx.navigateTo({ //跳转页面
      url: '/pages/index/index'
    })
  },
  //显示加载中Toast
  showToast() {
    this.setData({
      showLoading: true //显示加载中Toast
    })
    Toast.loading({
      message: '加载中...',
      forbidClick: true,
      loadingType: 'spinner',
      duration: 0,
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.showToast()
    this.getVenue()
    this.getCourtType()
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    // seedIndex = seedTitle.length;//存储最后一个种子下标
    // console.log(seedIndex)
    // console.log(seedTitle)
    var that = this
    if (that.data.showAll != 1) {
      this.showToast()
      that.data.page = that.data.page + 1;
      // this.getWorks();
      console.log(that.data.page)
      that.getVenue()
      wx.showNavigationBarLoading();
    } else {
      console.log("已加载完")
    }
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})