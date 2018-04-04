from app import db

class Strategy(db.Model):
    __tablename__ = "strategy"

    id = db.Column(db.Integer, primary_key=True)
    sg_id = db.Column(db.Integer, db.ForeignKey('attr_ch.id'))
    pg_id = db.Column(db.Integer, db.ForeignKey('attr_ch.id'))
    sf_id = db.Column(db.Integer, db.ForeignKey('attr_ch.id'))
    pf_id = db.Column(db.Integer, db.ForeignKey('attr_ch.id'))
    c_id = db.Column(db.Integer, db.ForeignKey('attr_ch.id'))
    v_sg_id = db.Column(db.Integer, db.ForeignKey('attr_ch.id'))
    v_pg_id = db.Column(db.Integer, db.ForeignKey('attr_ch.id'))
    v_sf_id = db.Column(db.Integer, db.ForeignKey('attr_ch.id'))
    v_pf_id = db.Column(db.Integer, db.ForeignKey('attr_ch.id'))
    v_c_id = db.Column(db.Integer, db.ForeignKey('attr_ch.id'))

    def __init__(self, sg_id, pg_id, sf_id, pf_id, c_id,
                 v_sg_id, v_pg_id, v_sf_id, v_pf_id, v_c_id):
        (self.sg_id, self.pg_id, self.sf_id, self.pf_id, self.c_id,
        self.v_sg_id, self.v_pg_id, self.v_sf_id, self.v_pf_id, self.v_c_id )= (
            sg_id, pg_id, sf_id, pf_id, c_id, v_sg_id, v_pg_id, v_sf_id, v_pf_id, v_c_id
        )

    def __repr__(self):
        return "<Strategy %r>" % self.id


class AttrCh(db.Model):
    __tablename__ = 'attr_ch'
    id = db.Column(db.Integer, primary_key=True)
    strategy_index = db.Column(db.String(255))
    fg_pct = db.Column(db.FLOAT)
    three_pt_pct = db.Column(db.FLOAT)
    fta_pct = db.Column(db.FLOAT)
    oreb_pct = db.Column(db.FLOAT)
    dreb_pct = db.Column(db.FLOAT)
    ast_pct = db.Column(db.FLOAT)
    tov_pct = db.Column(db.FLOAT)
    stl_pct = db.Column(db.FLOAT)
    blk_pct = db.Column(db.FLOAT)
    pf_pct = db.Column(db.FLOAT)

    def __init__(self, strategy_index, fg_pct, three_pt_pct, fta_pct, oreb_pct, dreb_pct, ast_pct, tov_pct, stl_pct, blk_pct, pf_pct):
        (self.fg_pct, self.three_pt_pct, self.fta_pct, self.oreb_pct, self.dreb_pct, self.ast_pct, self.tov_pct, self.stl_pct,
         self.blk_pct, self.pf_pct) = (fg_pct, three_pt_pct, fta_pct, oreb_pct, dreb_pct, ast_pct, tov_pct, stl_pct,
                                      blk_pct, pf_pct)

    def __repr__(self):
        return "<Strategy %r>" % self.id
