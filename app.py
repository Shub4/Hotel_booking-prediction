from flask import Flask, request, render_template
#from flask_cors import cross_origin
#import sklearn
import pickle
import pandas as pd
from keras.models import load_model



app = Flask(__name__)


@app.route('/', methods=('GET' , 'POST'))

def predict():
    
    
    if request.method == "POST":

        Age = int(request.form.get('age'))
        DaysSinceCreation = int(request.form.get('creation'))
        AverageLeadTime = int(request.form.get('lead'))
        PersonsNights = int(request.form.get('stay'))
        LodgingRevenue = float(request.form.get('revenue'))
        


        nationality=request.form.get('nation')
        
        if(nationality=='DEU'):
            Nationality_DEU = 1
            Nationality_ESP = 0
            Nationality_FRA = 0
            Nationality_OTHER = 0
            Nationality_PRT = 0
            Nationality_USA = 0
            

        elif (nationality=='ESP'):
            Nationality_DEU = 0
            Nationality_ESP = 1
            Nationality_FRA = 0
            Nationality_OTHER = 0
            Nationality_PRT = 0
            Nationality_USA = 0
        
        elif (nationality=='FRA'):
            Nationality_DEU = 0
            Nationality_ESP = 0
            Nationality_FRA = 1
            Nationality_OTHER = 0
            Nationality_PRT = 0
            Nationality_USA = 0
            
        elif (nationality=='PRT'):
            Nationality_DEU = 0
            Nationality_ESP = 0
            Nationality_FRA = 0
            Nationality_OTHER = 0
            Nationality_PRT = 1
            Nationality_USA = 0
            
        elif (nationality=='USA'):
            Nationality_DEU = 0
            Nationality_ESP = 0
            Nationality_FRA = 0
            Nationality_OTHER = 0
            Nationality_PRT = 0
            Nationality_USA = 1
            
        else:
            Nationality_DEU = 0
            Nationality_ESP = 0
            Nationality_FRA = 0
            Nationality_OTHER = 1
            Nationality_PRT = 0
            Nationality_USA = 0
            
        
        
        dist = request.form.get("distribution")
        if (dist == 'Electronic'):
            d_elect = 1
            d_travel = 0
        
        else:
            d_elect = 0
            d_travel = 1
         

    
        seg = request.form.get("segment")
        if (seg == 'Corporate'):
            m_corporate = 1
            m_direct = 0
            m_group = 0
            m_travel = 0
        
        elif (seg == 'Direct'):
            m_corporate = 0
            m_direct = 1
            m_group = 0
            m_travel = 0

        elif (seg == 'Groups'):
            m_corporate = 0
            m_direct = 0
            m_group = 1
            m_travel = 0

        else:
            m_corporate = 0
            m_direct = 0
            m_group = 0
            m_travel = 1
            
        OtherRevenue = 67.89
        SRCrib = 0
        SRKingSizeBed = 0
        SRTwinBed = 0

        val=[[Age, DaysSinceCreation, AverageLeadTime, LodgingRevenue, OtherRevenue, 
              PersonsNights, SRCrib, SRKingSizeBed, SRTwinBed,
              Nationality_DEU, Nationality_ESP, Nationality_FRA, Nationality_OTHER,
              Nationality_PRT, Nationality_USA, d_elect, d_travel, m_corporate,
              m_direct, m_group, m_travel]]
        
        cols=['Age', 'DaysSinceCreation', 'AverageLeadTime', 'LodgingRevenue',
       'OtherRevenue', 'PersonsNights', 'SRCrib', 'SRKingSizeBed', 'SRTwinBed',
       'Nationality_DEU', 'Nationality_ESP', 'Nationality_FRA',
       'Nationality_OTHER', 'Nationality_PRT', 'Nationality_USA',
       'DistributionChannel_Electronic Distribution',
       'DistributionChannel_Travel Agent/Operator', 'MarketSegment_Corporate',
       'MarketSegment_Direct', 'MarketSegment_Groups',
       'MarketSegment_Travel Agent/Operator']
        
        
        model = load_model('model_ann.h5')
        scale = pickle.load(open('scale_data.pkl', "rb"))
        
        df=pd.DataFrame(val, columns=cols)
        var=scale.transform(df)
        df_new=pd.DataFrame(var, columns=cols)
        df_new
        
        pred=model.predict(df_new)
        
        prediction=[]
        if pred>=0.5:
            prediction.append(1)
        else:
            prediction.append(0)
            
        output=prediction[0]
        
    else:
        output=""
        
    return render_template('test.html',prediction=output)



if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
