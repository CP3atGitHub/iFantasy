from flask import Blueprint

from flask_restful import Api, Resource,reqparse
from app import db
from app.model.tactics import OStrategy,AttrCh, DStrategy
from app.model.team import BagPlayer,LineUp,SeasonData,PlayerBase

tactics_bp = Blueprint("tactics_bp", __name__)
tactics_api = Api(tactics_bp)


query = db.session.query

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



#进攻战术介绍
class Offense_strategy_IndexAPi(Resource):
    def get(self, key):
        return OFFENSE_STRATEGY[key]

#防守战术介绍
class Defense_Strategy_IndexAPi(Resource):
    def get(self, key):
        return DEFENSE_STRATEGY[key]

class Score_APi(Resource):
    def get(self):
        parser =reqparse.RequestParser()
        parser.add_argument("user_id", type=int)
        def get(self):
            args = self.parser.parse_args()
            user_id = args['user_id']
            data = query(LineUp).filter_by(user_id=user_id).all()
            pg = data.pg
            sg = data.sg
            sf = data.sf
            pf = data.pf
            c = data.c
            pg_data = query(BagPlayer).filter_by(id=pg).all()
            sg_data = query(BagPlayer).filter_by(id=sg).all()
            sf_data = query(BagPlayer).filter_by(id=sf).all()
            pf_data = query(BagPlayer).filter_by(id=pf).all()
            c_data = query(BagPlayer).filter_by(id=c).all()
            return  pg_data.score+sg_data.score+sf_data.score+pf_data.score+c_data.score




#请一个用户ID下来，通过用户ID访问阵容，利用阵容中的球员ID访问球员的SeasonData
class  Strategy_RecommendAPi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("user_id", type=int)
    def get(self):
        args = self.parser.parse_args()
        user_id = args['user_id']
        data = query(LineUp).filter_by(user_id=user_id).all()
        pg = data.pg
        sg = data.sg
        sf = data.sf
        pf = data.pf
        c = data.c
        for each in data:
            if query(SeasonData).filter_by(player_id=pg).first() or query(SeasonData).filter_by(player_id=sg).first()\
                    or query(SeasonData).filter_by(player_id=sf).first():
                random1 = query(SeasonData).filter_by(player_id=pg).all()
                random2 = query(SeasonData).filter_by(player_id=sg).all()
                random3 = query(SeasonData).filter_by(player_id=sf).all()
                if random1.fg_3pt > 0.33 or random2.fg_3pt > 0.33 or random2.fg_3pt > 0.33:
                    recommend = 2
                    return recommend
            elif query(SeasonData).filter_by(player_id=pg).first() or query(SeasonData).filter_by(player_id=sf).first():
                random1 = query(SeasonData).filter_by(player_id=pg).all()
                random2 = query(SeasonData).filter_by(player_id=sf).all()
                if random1.fg_3pt > 0.33 or random2.fg_3pt > 0.33:
                    recommend = 1
                    return recommend
            #elif query(SeasonData).filterby()


class OffStrategy_InstallAPi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("offstrategy_id" ,type=int)
    def get(self):
        args = self.parser.parse_args()
        offstrategy_id = args['offstrategy_id']
        data = query(OStrategy).filter_by(offstrategy_id=id)
        if data is not None:
            return data

class DefStrategy_InstallAPi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("defstrategy_id" ,type=int)
    def get(self):
        args = self.parser.parse_args()
        defstrategy_id = args['defstrategy_id']
        data = query(DStrategy).filter_by(defstrategy_id=id)
        if data is not None:
            return data

tactics_api.add_resource(Offense_strategy_IndexAPi,'/off_strategy/<key>')

tactics_api.add_resource(Defense_Strategy_IndexAPi,'/def_strategy/<key>')

tactics_api.add_resource(Strategy_RecommendAPi,'/strategy_recommend')

tactics_api.add_resource(Score_APi,'/score')

tactics_api.add_resource(OffStrategy_InstallAPi,'/offstrategy_install')

tactics_api.add_resource(DefStrategy_InstallAPi,'/defstrategy_install')

