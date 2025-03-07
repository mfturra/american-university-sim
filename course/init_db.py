from app import create_app, db
from models import Institution, Degree

app = create_app()
# create_institution = False
# if create_institution:
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
    # db.drop_all()

    # create necessary tables based on classes
    db.create_all()

    # add entries to respective Institution class' table
    db.session.add_all([public_uni, private_uni, community_uni])

    # commit the change to the database
    db.session.commit()

    # add STEM degrees to public university
    pub_degree0 = Degree(degree_track='STEM', degree_name='Biology',
                    degree_desc="Study of living organisms and life processes.", curriculum_difficulty=7,
                    uni_id=public_uni.id)
    pub_degree1 =  Degree(degree_track='STEM', degree_name='Computer Science',
                    degree_desc="Programming, algorithms, and software development.", curriculum_difficulty=8,
                    uni_id=public_uni.id)
    pub_degree2 =  Degree(degree_track='STEM', degree_name='Electrical Engineering',
                    degree_desc="Designing and developing electrical systems.", curriculum_difficulty=9,
                    uni_id=public_uni.id)
    pub_degree3 =  Degree(degree_track='STEM', degree_name='Mathematics',
                    degree_desc="Abstract concepts, theories, and problem-solving.", curriculum_difficulty=8,
                    uni_id=public_uni.id)
    pub_degree4 =  Degree(degree_track='STEM', degree_name='Physics',
                    degree_desc="Understanding the laws of nature and the universe.", curriculum_difficulty=9,
                    uni_id=public_uni.id)
    
    # add business degrees to public university
    pub_degree5 = Degree(degree_track='Business', degree_name='Accounting',
                    degree_desc="Managing financial records and ensuring accuracy.", curriculum_difficulty=7,
                    uni_id=public_uni.id)
    pub_degree6 =  Degree(degree_track='Business', degree_name='Economics',
                    degree_desc="Study of resource allocation and economic systems.", curriculum_difficulty=8,
                    uni_id=public_uni.id)
    pub_degree7 =  Degree(degree_track='Business', degree_name='Finance',
                    degree_desc="Managing investments, assets, and financial planning.", curriculum_difficulty=7,
                    uni_id=public_uni.id)
    pub_degree8 =  Degree(degree_track='Business', degree_name='Marketing',
                    degree_desc="Promoting products and understanding consumer behavior.", curriculum_difficulty=5,
                    uni_id=public_uni.id)
    pub_degree9 =  Degree(degree_track='Business', degree_name='Business Management',
                    degree_desc="Overseeing operations and organizational leadership.", curriculum_difficulty=6,
                    uni_id=public_uni.id)
    
    # add humanities degrees to public university
    pub_degree10 = Degree(degree_track='Humanities', degree_name='English',
                    degree_desc="Literature, writing, and critical analysis of texts.", curriculum_difficulty=5,
                    uni_id=public_uni.id)
    pub_degree11 =  Degree(degree_track='Humanities', degree_name='History',
                    degree_desc="Study of past events and their impact", curriculum_difficulty=6,
                    uni_id=public_uni.id)
    pub_degree12 =  Degree(degree_track='Humanities', degree_name='Philosophy',
                    degree_desc="Exploration of fundamental questions about existence and knowledge.", curriculum_difficulty=7,
                    uni_id=public_uni.id)
    pub_degree13 =  Degree(degree_track='Humanities', degree_name='Political Science',
                    degree_desc="Analysis of political systems and governmental structures.", curriculum_difficulty=6,
                    uni_id=public_uni.id)
    pub_degree14 =  Degree(degree_track='Humanities', degree_name='Psychology',
                    degree_desc="Understanding human behavior and mental processes.", curriculum_difficulty=6,
                    uni_id=public_uni.id)

    ## add STEM degrees to public university
    prv_degree0 =   Degree(degree_track='STEM', degree_name='Biology',
                    degree_desc="Study of living organisms and life processes.", curriculum_difficulty=7,
                    uni_id=private_uni.id)
    prv_degree1 =   Degree(degree_track='STEM', degree_name='Computer Science',
                    degree_desc="Programming, algorithms, and software development.", curriculum_difficulty=8,
                    uni_id=private_uni.id)
    prv_degree2 =   Degree(degree_track='STEM', degree_name='Electrical Engineering',
                    degree_desc="Designing and developing electrical systems.", curriculum_difficulty=9,
                    uni_id=private_uni.id)
    prv_degree3 =   Degree(degree_track='STEM', degree_name='Mathematics',
                    degree_desc="Abstract concepts, theories, and problem-solving.", curriculum_difficulty=8,
                    uni_id=private_uni.id)
    prv_degree4 =   Degree(degree_track='STEM', degree_name='Physics',
                    degree_desc="Understanding the laws of nature and the universe.", curriculum_difficulty=9,
                    uni_id=private_uni.id)
    
    # add business degrees to public university
    prv_degree5 =   Degree(degree_track='Business', degree_name='Accounting',
                    degree_desc="Managing financial records and ensuring accuracy.", curriculum_difficulty=7,
                    uni_id=private_uni.id)
    prv_degree6 =   Degree(degree_track='Business', degree_name='Economics',
                    degree_desc="Study of resource allocation and economic systems.", curriculum_difficulty=8,
                    uni_id=private_uni.id)
    prv_degree7 =   Degree(degree_track='Business', degree_name='Finance',
                    degree_desc="Managing investments, assets, and financial planning.", curriculum_difficulty=7,
                    uni_id=private_uni.id)
    prv_degree8 =   Degree(degree_track='Business', degree_name='Marketing',
                    degree_desc="Promoting products and understanding consumer behavior.", curriculum_difficulty=5,
                    uni_id=private_uni.id)
    prv_degree9 =   Degree(degree_track='Business', degree_name='Business Management',
                    degree_desc="Overseeing operations and organizational leadership.", curriculum_difficulty=6,
                    uni_id=private_uni.id)
    
    # add humanities degrees to public university
    prv_degree10 = Degree(degree_track='Humanities', degree_name='English',
                    degree_desc="Literature, writing, and critical analysis of texts.", curriculum_difficulty=5,
                    uni_id=private_uni.id)
    prv_degree11 =  Degree(degree_track='Humanities', degree_name='History',
                    degree_desc="Study of past events and their impact", curriculum_difficulty=6,
                    uni_id=private_uni.id)
    prv_degree12 =  Degree(degree_track='Humanities', degree_name='Philosophy',
                    degree_desc="Exploration of fundamental questions about existence and knowledge.", curriculum_difficulty=7,
                    uni_id=private_uni.id)
    prv_degree13 =  Degree(degree_track='Humanities', degree_name='Political Science',
                    degree_desc="Analysis of political systems and governmental structures.", curriculum_difficulty=6,
                    uni_id=private_uni.id)
    prv_degree14 =  Degree(degree_track='Humanities', degree_name='Psychology',
                    degree_desc="Understanding human behavior and mental processes.", curriculum_difficulty=6,
                    uni_id=private_uni.id)

    ## add STEM degrees to community college
    cc_degree0 =   Degree(degree_track='STEM', degree_name='Biology',
                    degree_desc="Study of living organisms and life processes.", curriculum_difficulty=7,
                    uni_id=community_uni.id)
    cc_degree1 =   Degree(degree_track='STEM', degree_name='Computer Science',
                    degree_desc="Programming, algorithms, and software development.", curriculum_difficulty=8,
                    uni_id=community_uni.id)
    cc_degree2 =   Degree(degree_track='STEM', degree_name='Electrical Engineering',
                    degree_desc="Designing and developing electrical systems.", curriculum_difficulty=9,
                    uni_id=community_uni.id)
    cc_degree3 =   Degree(degree_track='STEM', degree_name='Physics',
                    degree_desc="Understanding the laws of nature and the universe.", curriculum_difficulty=9,
                    uni_id=community_uni.id)
    
    # add business degrees to public university
    cc_degree4 =   Degree(degree_track='Business', degree_name='Accounting',
                    degree_desc="Managing financial records and ensuring accuracy.", curriculum_difficulty=7,
                    uni_id=community_uni.id)
    cc_degree5 =   Degree(degree_track='Business', degree_name='Finance',
                    degree_desc="Managing investments, assets, and financial planning.", curriculum_difficulty=7,
                    uni_id=community_uni.id)
    cc_degree6 =   Degree(degree_track='Business', degree_name='Marketing',
                    degree_desc="Promoting products and understanding consumer behavior.", curriculum_difficulty=5,
                    uni_id=community_uni.id)
    cc_degree7 =   Degree(degree_track='Business', degree_name='Business Management',
                    degree_desc="Overseeing operations and organizational leadership.", curriculum_difficulty=6,
                    uni_id=community_uni.id)
    
    # add humanities degrees to public university
    cc_degree8 = Degree(degree_track='Humanities', degree_name='English',
                    degree_desc="Literature, writing, and critical analysis of texts.", curriculum_difficulty=5,
                    uni_id=community_uni.id)
    cc_degree9 =  Degree(degree_track='Humanities', degree_name='History',
                    degree_desc="Study of past events and their impact", curriculum_difficulty=6,
                    uni_id=community_uni.id)
    cc_degree10 =  Degree(degree_track='Humanities', degree_name='Philosophy',
                    degree_desc="Exploration of fundamental questions about existence and knowledge.", curriculum_difficulty=7,
                    uni_id=community_uni.id)
    cc_degree11 =  Degree(degree_track='Humanities', degree_name='Psychology',
                    degree_desc="Understanding human behavior and mental processes.", curriculum_difficulty=6,
                    uni_id=community_uni.id)

    db.session.add_all([pub_degree0, pub_degree1, pub_degree2, pub_degree3, pub_degree4, pub_degree5, pub_degree6, pub_degree7, pub_degree8, pub_degree9, pub_degree10, pub_degree11, pub_degree12, pub_degree13, pub_degree14])
    db.session.add_all([prv_degree0, prv_degree1, prv_degree2, prv_degree3, prv_degree4, prv_degree5, prv_degree6, prv_degree7, prv_degree8, prv_degree9, prv_degree10, prv_degree11, prv_degree12, prv_degree13, prv_degree14])
    db.session.add_all([cc_degree0, cc_degree1, cc_degree2, cc_degree3, cc_degree4, cc_degree5, cc_degree6, cc_degree7, cc_degree8, cc_degree9, cc_degree10, cc_degree11])

    db.session.commit()