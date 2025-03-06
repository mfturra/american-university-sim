from app import create_app, db
from models import Institution, Degree

app = create_app()
create_institution = False
if create_institution:

    public_uni =    Institution(inst_type='Education', uni_name='Public University',
                    uni_type='Public', uni_welcome="greetings from the public university",
                    uni_cost=25000.00)
    private_uni =   Institution(inst_type='Education', uni_name='Private University',
                    uni_type='Private', uni_welcome="greetings from the private university",
                    uni_cost=45000.00)
    community_uni = Institution(inst_type='Education', uni_name='Community College', 
                    uni_type='Community', uni_welcome="greetings from the community college",
                    uni_cost=2500.00)
if create_institution == False:
    public_uni = 1
    private_uni = 2
    community_uni = 3


with app.app_context():
    db.drop_all()
    db.create_all()
    # db.session.add_all([public_uni, private_uni, community_uni])
    db.session.commit()

    # add business degrees to public university
    # pub_degree1 = Degree(degree_track='STEM', degree_name='Biology',
    #                 degree_desc="Adding numbers together.", curriculum_difficulty=7,
    #                 uni_id=public_uni.id)
    pub_degree2 =  Degree(degree_track='STEM', degree_name='Computer Science',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=8,
                    uni_id=public_uni)
    pub_degree3 =  Degree(degree_track='STEM', degree_name='Electrical Engineering',
                    degree_desc="Evaluating local market standings.", curriculum_difficulty=9,
                    uni_id=public_uni)
    pub_degree4 =  Degree(degree_track='STEM', degree_name='Mathematics',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=8,
                    uni_id=public_uni)
    pub_degree5 =  Degree(degree_track='STEM', degree_name='Physics',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=9,
                    uni_id=public_uni)

    # add business degrees to private university
    # prv_degree1 = Degree(degree_track='STEM', degree_name='Biology',
    #                 degree_desc="Adding numbers together.", curriculum_difficulty=7,
    #                 uni_id=private_uni)
    prv_degree2 =  Degree(degree_track='STEM', degree_name='Computer Science',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=8,
                    uni_id=private_uni)
    prv_degree3 =  Degree(degree_track='STEM', degree_name='Electrical Engineering',
                    degree_desc="Evaluating local market standings.", curriculum_difficulty=9,
                    uni_id=private_uni)
    prv_degree4 =  Degree(degree_track='STEM', degree_name='Mathematics',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=8,
                    uni_id=private_uni)
    prv_degree5 =  Degree(degree_track='STEM', degree_name='Physics',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=9,
                    uni_id=private_uni)

    # add business degrees to community college
    cc_degree1 = Degree(degree_track='STEM', degree_name='Biology',
                    degree_desc="Adding numbers together.", curriculum_difficulty=7,
                    uni_id=community_uni)
    cc_degree2 =  Degree(degree_track='STEM', degree_name='Computer Science',
                    degree_desc="Evaluating local market standings.", curriculum_difficulty=8,
                    uni_id=community_uni)
    cc_degree3 =  Degree(degree_track='STEM', degree_name='Electrical Engineering',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=9,
                    uni_id=community_uni)
    cc_degree4 =  Degree(degree_track='STEM', degree_name='Physics',
                    degree_desc="Evaluating world markets.", curriculum_difficulty=9,
                    uni_id=community_uni)

    db.session.add_all([pub_degree2, pub_degree3, pub_degree4, pub_degree5])
    db.session.add_all([prv_degree2, prv_degree3, prv_degree4, prv_degree5])
    db.session.add_all([cc_degree1, cc_degree2, cc_degree3, cc_degree4])

    db.session.commit()