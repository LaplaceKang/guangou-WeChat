//导入要请求的DjangoURL
import {
  DjangoURL
} from '../../utils/util.js'
import {
  Map_CourtType
} from '../../utils/typeMap.js'
import Toast from '../../miniprogram/miniprogram_npm/weapp/toast/toast';

Page({
  /**
   * 页面的初始数据
   */
  data: {
    option1: [{
      text: '区域',
      value: 0
    }, ],
    option2: [{
      text: '全部',
      value: '0'
    }, ],
    option3: [{
      text: '智能排序',
      value: 3
    }, ],
    option4: [{
      text: '筛选',
      value: 6
    }, ],
    value1: 0,
    value2: 0,
    value3: 3,
    value4: 6,
    venue: [],
    page: 1, //显示第一页
    showLoading: true, //显示加载中Toast
  },
  //显示全部运动类型
  getAllVenue() {
    var that = this
    wx.request({
      url: DjangoURL + 'wx/venue/getIndexVenue?cityid=' + that.data.cityid + '&longitude=' + that.data.longitude + '&latitude=' + that.data.latitude + '&page=' + that.data.page,
      method: "GET",
      success: function (res) {
        that.setData({
          venue: that.data.venue.concat(res.data.data),
          showAll: res.data.showAll,
          showLoading: false //隐藏加载中Toast
        })
        // console.log(res.data)
        // console.log(res.data.showAll)
      }
    })
  },
  //根据运动类型筛选总场馆
  getVenue: function (courttypeid) {
    var that = this
    if (courttypeid != 0) {
      wx.request({
        url: DjangoURL + 'wx/venue/filterCourtType?cityid=' + that.data.cityid + '&courttypeid=' + courttypeid + '&longitude=' + that.data.longitude + '&latitude=' + that.data.latitude+'&page='+that.data.page,
        method: "GET",
        success: function (res) {
          that.setData({
            venue: that.data.venue.concat(res.data.data),
            showAll: res.data.showAll,
            showLoading: false //隐藏加载中Toast
          })
          // console.log(res.data.data)
        }
      })
    } else { //显示全部场馆
      that.getAllVenue()
    }
  },
  //从util中获取总场馆运动类型
  getAllCourtType() {
    let that = this
    for (let i = 1; i <= Object.keys(Map_CourtType).length; i++) {
      // console.log(Map_CourtType[i+''])
      // console.log(that.data.option2)
      that.data.option2.push({
        text: Map_CourtType[i + ''][0],
        value: i + ''
      })
    }
    //必须真正赋值，才能刷新页面
    that.setData({
      option2: that.data.option2
    })
  },
  //切换运动类型
  changeType(value) {
    // console.log(value.detail)
    this.data.venue = [] //先清空之前的数据
    this.data.page=1
    this.showToast()
    this.getVenue(value.detail)
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
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    // console.log(options)
    // console.log(options.courttypeid)
    that.setData({
      courttypeid: options.courttypeid,
      latitude: options.latitude,
      longitude: options.longitude,
      cityid: options.cityid,
      value2: options.courttypeid,
    })
    that.getAllCourtType()
    that.getVenue(options.courttypeid)
    that.showToast()
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {},

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
    var that = this
    if (that.data.showAll != 1) {
      that.showToast()
      that.data.page = that.data.page + 1;
      // this.getWorks();
      console.log(that.data.page)
      that.getVenue(that.data.courttypeid)
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