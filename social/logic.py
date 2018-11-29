import datetime

from user.models import User
from social.models import Swiped
from social.models import Friend


def get_rcmd_users(user):
    '''
    获取推荐用户

       max_year        min_year     current_year
    ----|-----------------|----------------|--------------|-------->
                                          2018           2019
    '''
    sex = user.profile.dating_sex
    location = user.profile.location
    min_age = user.profile.min_dating_age
    max_age = user.profile.max_dating_age

    current_year = datetime.date.today().year
    min_year = current_year - min_age
    max_year = current_year - max_age

    users = User.objects.filter(sex=sex, location=location,
                                birth_year__gte=max_year,
                                birth_year__lte=min_year)

    return users


def like(user, sid):
    '''喜欢一个用户'''
    Swiped.mark(user.id, sid, 'like')
    # 检查被滑动的用户是否喜欢过自己
    if Swiped.is_liked(sid, user.id):
        Friend.be_friends(user.id, sid)
