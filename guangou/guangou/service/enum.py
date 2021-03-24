from enum import Enum, unique


@unique
class SitePeriodStateEnum(Enum):
    Available = 1               # 可预定
    Booked = 2                  # 已预订
    SchoolCourse = 3            # 上课
    Maintenance = 4             # 检修
    Disable = 5                 # 不可用
    LongTermBooked = 6          # 长期预订
    BindBooked = 7              # 捆绑预订
    PrimePeriodBooked = 8       # 黄金时段预订
    CountedCardBooked = 9       # 次卡预订


@unique
class OrderStateEnum(Enum):
    Unpaid = 1                  # 待支付
    Unused = 2                  # 待使用
    Used = 3                    # 已使用
    Canceled = 4                # 已取消
    PaidLongTerm = 5            # 已支付（长期预订）
    PaidAppend = 6              # 已支付（补加订单）

