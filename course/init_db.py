from app import create_app, db
from models import Institution, Degree

app = create_app()

public_uni =    Institution(inst_type='Education', uni_name='Public University',
                 uni_type='Public', uni_welcome="greetings from the public university",
                 uni_cost=25000.00)
private_uni =   Institution(inst_type='Education', uni_name='Private University',
                 uni_type='Private', uni_welcome="greetings from the private university",
                 uni_cost=45000.00)
community_uni = Institution(inst_type='Education', uni_name='Community College', 
                 uni_type='Community', uni_welcome="greetings from the community college",
                 uni_cost=2500.00)

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add_all([public_uni, private_uni, community_uni])
    db.session.commit()

    # add business degrees to public university
    pub_acct_degree = Degree(degree_track='Business', degree_name='Accounting',
                    degree_desc="Adding numbers together.", curriculum_difficulty=7,
                    uni_id=public_uni.id)
    pub_econ_degree =  Degree(degree_track='Business', degree_name='Economics',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=8,
                    uni_id=public_uni.id)
    pub_fin_degree =  Degree(degree_track='Business', degree_name='Finance',
                    degree_desc="Evaluating local market standings.", curriculum_difficulty=7,
                    uni_id=public_uni.id)
    pub_mkt_degree =  Degree(degree_track='Business', degree_name='Marketing',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=5,
                    uni_id=public_uni.id)
    pub_mng_degree =  Degree(degree_track='Business', degree_name='Business Management',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=6,
                    uni_id=public_uni.id)

    # add business degrees to private university
    prv_acct_degree = Degree(degree_track='Business', degree_name='Accounting',
                    degree_desc="Adding numbers together.", curriculum_difficulty=7,
                    uni_id=private_uni.id)
    prv_econ_degree =  Degree(degree_track='Business', degree_name='Economics',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=8,
                    uni_id=private_uni.id)
    prv_fin_degree =  Degree(degree_track='Business', degree_name='Finance',
                    degree_desc="Evaluating local market standings.", curriculum_difficulty=7,
                    uni_id=private_uni.id)
    prv_mkt_degree =  Degree(degree_track='Business', degree_name='Marketing',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=5,
                    uni_id=private_uni.id)
    prv_mng_degree =  Degree(degree_track='Business', degree_name='Business Management',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=6,
                    uni_id=private_uni.id)

    # add business degrees to community college
    cc_acct_degree = Degree(degree_track='Business', degree_name='Accounting',
                    degree_desc="Adding numbers together.", curriculum_difficulty=7,
                    uni_id=community_uni.id)
    cc_fin_degree =  Degree(degree_track='Business', degree_name='Finance',
                    degree_desc="Evaluating local market standings.", curriculum_difficulty=7,
                    uni_id=community_uni.id)
    cc_mkt_degree =  Degree(degree_track='Business', degree_name='Marketing',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=5,
                    uni_id=community_uni.id)
    cc_mng_degree =  Degree(degree_track='Business', degree_name='Business Management',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=6,
                    uni_id=community_uni.id)

    db.session.add_all([pub_acct_degree, pub_econ_degree, pub_fin_degree, pub_mkt_degree, pub_mng_degree])
    db.session.add_all([prv_acct_degree, prv_econ_degree, prv_fin_degree, prv_mkt_degree, prv_mng_degree])
    db.session.add_all([cc_acct_degree, cc_fin_degree, cc_mkt_degree, cc_mng_degree])

    db.session.commit()