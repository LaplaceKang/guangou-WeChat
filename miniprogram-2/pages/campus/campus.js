import Toast from '../../miniprogram/miniprogram_npm/weapp/toast/toast';
import {
  Map_Facility
} from '../../utils/typeMap.js'
//导入要请求的DjangoURL
import {
  DjangoURL
} from '../../utils/util.js'

Page({
  /**
   * 页面的初始数据
   */
  data: {
    imgUrls: [
      "/images/4.jpg",
      "/images/4.jpg",
      "/images/4.jpg"
    ],
    selectCourtIndex: 0,
    showLoading: true
  },
  //事件处理函数
  toupper: function () {
    console.log("触发了toupper");
  },
  //获取总场馆信息
  getVenueDetail() {
    var that = this
    wx.request({
      url: DjangoURL+'wx/venue/getVenueDetail?venueid=' + that.data.venueid + '&courttypeid=' + that.data.courttype[0].courttypeid,
      method: "GET",
      success: function (res) {
        that.setData({
          venue: res.data.data.venue
        })
        that.getCourtDetail(0)
        // console.log(res.data)
      }
    })
  },
  //获取场馆的信息
  getCourtDetail(courtTypeIndex) {
    let that = this
    wx.request({
      url: DjangoURL+'wx/court/getCourtDetail?venueid=' + that.data.venueid + '&courttypeid=' + that.data.courttype[courtTypeIndex].courttypeid,
      method: "GET",
      success: function (res) {
        let court = res.data.data.court
        court.facilityname = []
        for (let i = 0; i < court.facilityid.length; i++) {
          //根据facilityid的值来添加，而不是下标
          court.facilityname.push(Map_Facility[court.facilityid[i] + ''])
        }
        that.data.allCourt[courtTypeIndex] = court
        // console.log(court)
        that.setData({
          court: court,
          showLoading: false//隐藏加载中Toast
        })
      }
    })
  },
  //切换场馆类型
  selectCourtType(event) {
    let that = this
    let index = event.detail.index
    that.setData({
      selectCourtIndex: index
    })
    // console.log(event.detail.index)
    // console.log(that.data.allCourt[index])
    if (that.data.allCourt[index] == null) {
      this.getCourtDetail(event.detail.index)
    } else {
      that.setData({
        court: that.data.allCourt[index]
      })
    }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this
    // console.log(options)
    let courttype = JSON.parse(options.courttype) //字符串转JSON
    that.setData({
      courttype: courttype,
      venuename: options.venuename,
      venueid: options.venueid,
      longitude: options.longitude,
      latitude: options.latitude,
      allCourt: new Array(courttype.length)
    })
    this.getVenueDetail()
    Toast.loading({
      message: '加载中...',
      forbidClick: true,
      loadingType: 'spinner',
      duration:0,
    });
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {},

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {},

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

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})