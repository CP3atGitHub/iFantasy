from flask import Blueprint

from flask_restful import Api, Resource,reqparse
from app.model.tactics import OStrategy,AttrCh, DStrategy

tactics_bp = Blueprint("tactics_bp", __name__)
tactics_api = Api(tactics_bp)

OFFENSE_STRATEGY = {
    'strategy_1': {'strategy': '外线投射：通过无球掩护为PG、SG、SF提供外线投篮机会，较为克制内线包夹，' \
                                               '内线联防的防守战术。适合拥有强力外线得分能力的PG、SG、SF的队伍。'},
    'strategy_2': {'strategy': '挡拆外切：挡拆人提到上线为持球人做墙，做墙后持球人持球冲击内线带走两个防守人，' \
                        '并随时准备将球进行传导刚才挡拆者；做墙者来到甜点区准备出手中距离或三分球。此战术适用于有中远距离能力的内线球员。'},
    'strategy_3': {'strategy': '突破分球：本方队员篮下得分困难，中远距离投篮又没有机会时，' \
                                   '进攻队员可以选择突破分球，有目的地将对手挤向篮下，迫使对手缩小防守区域，' \
                                   '并及时将球传给跟进或绕到无人防守处的接应队员。这种突破分球的战术不是为了篮下得分，' \
                                   '而是为了给同伴中远距离投篮和空切上篮创造机会。'},
    'strategy_4': {'strategy': '内线强攻：清空强侧，给PF，C单打的机会。适合内线能力较强的球队。'},
    'strategy_5': {'strategy': '双塔战术：适用于同时拥有能力较强的PF、和C的球队，双塔战术利用两个球员强大的内线牵制力，' \
                                  '对对手内线造成更大的破坏。'},
    'strategy_6': {'strategy': '掩护内切：挡拆人提到上线为持球人做墙，做墙后持球人持球冲击内线一侧带走两个防守人，' \
                                  '并随时准备将球进行传导刚才挡拆者；做墙者来到另一侧准备接球上篮。此战术适用于内线终结能力较强的球员。'},
    'strategy_7': {'strategy': '普林斯顿体系：普林斯顿强调中锋调度和人人为我，我为人人的概念，坚持团队篮球和团队精神' \
                                  '在全队能力值偏低的情况下，提升球队战力。'},
}

DEFENSE_STRATEGY = {
    'strategy_8': {'strategy': '外线紧逼：PG、SG、SF提升外防守效率，降低对方外线投射效率，增加对方失误数量。'},
    'strategy_9': {'strategy': '外线联防：对方PG、SG、SF有一个或两个为精英外线时，可采用联防，增加被包夹人失误率，' \
                                    '但同时提高空位球员命中率。'},
    'strategy_10': {'strategy': '内线包夹：对方C、PF能力值较高时，可采用包夹，增加失误率，增加未被包夹球员命中率。'},
    'strategy_11': {'strategy': '二三联防：五个球员位置基本固定，每个球员防守覆盖一定区域，二三联防强调团队整体的防守存在感，压迫对手持球，' \
                                    '增加对手失误。适用于每个人防守能力或几个球员防守一般的球员。'},
}


#strategy_1:pg||sg||sf(who > 35%) three_pt_pct up 3%
#strategy_2:pg||sf fg_pct up 2%
#strategy_3:sg||sf fg_pct_up 2%   three_pt_pct up 3%
#strategy_4:pf||c fg_pct up 2%
#strategy_5:pf&&c fg_pct up 3%
#strategy_6:sg||sf fg_pct up 2%
#strategy_7:pg&&sg&&sf&&pf&&c fg_pct up 1%
#strategy_8:pg&&sg&&sf stl_pct 3%
#strategy_9:pg&&sg||pg&&sf||sg&&sf stl_pct up 5%
#strategy_10:



class Offense_strategy_IndexAPi(Resource):
    def get(self, key):
        return OFFENSE_STRATEGY[key]


class Offense_StrategyAPi(Resource):

    def get(self, attr_id):
        data = AttrCh.query.filter_by(id=attr_id).all()


        result =[]
        for random in data:
            random_data = {}
            random_data['pg_id'] = random.pg_id
            random_data['sg_id'] = random.sg_id
            random_data['sf_id'] = random.sf_id
            random_data['pf_id'] = random.pf_id
            random_data['c_id'] = random.c_id

            result.append(random_data)

        return {'data': result}



class Defense_Strategy_IndexAPi(Resource):
    def get(self, key):
        return DEFENSE_STRATEGY[key]

class Defense_StrategyAPi(Resource):

    def get(self, strategy_id):
        data = AttrCh.query.filter_by(id=strategy_id).all( )

        result = []
        for random in data:
            random_data = {}
            random_data['pg_id'] = random.pg_id
            random_data['sg_id'] = random.sg_id
            random_data['sf_id'] = random.sf_id
            random_data['pf_id'] = random.pf_id
            random_data['c_id'] = random.c_id

            result.append(random_data)

        return {'data': result}


tactics_api.add_resource(Offense_strategy_IndexAPi,'/off_strategy/<key>')
tactics_api.add_resource(Offense_StrategyAPi,'/off_strategy/<int:strategy_id>')
tactics_api.add_resource(Defense_Strategy_IndexAPi,'/def_strategy/<key>')
tactics_api.add_resource(Defense_StrategyAPi,'/def_strategy/<int:strategy_id>')

