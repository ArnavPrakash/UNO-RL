import os
import pandas as pd
import numpy as np

from UNO_GAME.game import tournament
import config as conf

def main():

    run = tournament(
        iterations = conf.params['iterations'],
        algo       = conf.params['algorithm'],
        comment    = conf.params['logging'],
        agent_info = conf.params['model']
    )

    result = pd.concat([
        pd.Series(run[0], name='winner'), 
        pd.Series(run[1], name='turns')
    ], axis = 1)
    
    result["win_rate"] = np.where(result["winner"]==conf.player_name_1,1,0)
    result["win_rate"] = result["win_rate"].cumsum()/(result.index+1)

    q_vals = pd.DataFrame(run[2].q)
    q_vals.index.rename("id", inplace=True)

    if not os.path.exists("data"):
        os.makedirs("data")

    q_vals.to_csv("data/q-values.csv", index=True)
    result.to_csv("data/results.csv", index=False) 
    

if __name__ == "__main__":
    main()