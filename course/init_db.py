from app import db, Institution, Degree

public_uni =    Institution(inst_type='Education', uni_name='Public University',
                 uni_type='Public', uni_welcome="greetings",
                 uni_cost=25000.00)
private_uni =   Institution(inst_type='Education', uni_name='Private University',
                 uni_type='Private', uni_welcome="greetings",
                 uni_cost=45000.00)
community_uni = Institution(inst_type='Education', uni_name='Community College', 
                 uni_type='Private', uni_welcome="greetings",
                 uni_cost=2500.00)

# add business degrees to public university
pub_acct_degree = Degree(degree_track='Business', degree_name='Accounting',
                degree_desc="Adding numbers together.", curriculum_difficulty=7,
                uni_id=public_uni)
pub_econ_degree =  Degree(degree_track='Business', degree_name='Economics',
                degree_desc="Evaluating world markets.", curriculum_difficulty=8,
                uni_id=public_uni)
pub_fin_degree =  Degree(degree_track='Business', degree_name='Finance',
                degree_desc="Evaluating local market standings.", curriculum_difficulty=7,
                uni_id=public_uni)
pub_mkt_degree =  Degree(degree_track='Business', degree_name='Marketing',
                degree_desc="Evaluating world markets.", curriculum_difficulty=5,
                uni_id=public_uni)
pub_mng_degree =  Degree(degree_track='Business', degree_name='Business Management',
                degree_desc="Evaluating world markets.", curriculum_difficulty=6,
                uni_id=public_uni)

# add business degrees to private university
prv_acct_degree = Degree(degree_track='Business', degree_name='Accounting',
                degree_desc="Adding numbers together.", curriculum_difficulty=7,
                uni_id=private_uni)
prv_econ_degree =  Degree(degree_track='Business', degree_name='Economics',
                degree_desc="Evaluating world markets.", curriculum_difficulty=8,
                uni_id=private_uni)
prv_fin_degree =  Degree(degree_track='Business', degree_name='Finance',
                degree_desc="Evaluating local market standings.", curriculum_difficulty=7,
                uni_id=private_uni)
prv_mkt_degree =  Degree(degree_track='Business', degree_name='Marketing',
                degree_desc="Evaluating world markets.", curriculum_difficulty=5,
                uni_id=private_uni)
prv_mng_degree =  Degree(degree_track='Business', degree_name='Business Management',
                degree_desc="Evaluating world markets.", curriculum_difficulty=6,
                uni_id=private_uni)

# add business degrees to community college
cc_acct_degree = Degree(degree_track='Business', degree_name='Accounting',
                degree_desc="Adding numbers together.", curriculum_difficulty=7,
                uni_id=community_uni)
cc_fin_degree =  Degree(degree_track='Business', degree_name='Finance',
                degree_desc="Evaluating local market standings.", curriculum_difficulty=7,
                uni_id=community_uni)
cc_mkt_degree =  Degree(degree_track='Business', degree_name='Marketing',
                degree_desc="Evaluating world markets.", curriculum_difficulty=5,
                uni_id=community_uni)
cc_mng_degree =  Degree(degree_track='Business', degree_name='Business Management',
                degree_desc="Evaluating world markets.", curriculum_difficulty=6,
                uni_id=community_uni)

db.session.add_all([public_uni, private_uni, community_uni])
db.session.add_all([pub_acct_degree, pub_econ_degree, pub_fin_degree, pub_mkt_degree, pub_mng_degree])
db.session.add_all([prv_acct_degree, prv_econ_degree, prv_fin_degree, prv_mkt_degree, prv_mng_degree])
db.session.add_all([cc_acct_degree, cc_fin_degree, cc_mkt_degree, cc_mng_degree])

db.session.commit()