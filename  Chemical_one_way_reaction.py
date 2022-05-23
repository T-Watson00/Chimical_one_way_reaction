import numpy as np
import matplotlib.pyplot as plt

# define A and B are materials and C is the product generated by the reaction between A and B or between A and A.

def main():
    k = 0.05                    # [1/s]
    nA_initial = 1.5            # [mol]
    nB_initial = 50             # [mol]
    price_A = 400               # [円/mol]
    price_B = 200               # [円/mol]
    price_C = 2*np.power(10,6)  # [円/mol]
    price_separate = 50000      # [円/mol]
    price_react = 1000          # [円/s]
    dt = 0.001
    t_max = 200
    psuedo_first_order_reaction_analysis(k,nA_initial,nB_initial,price_A,price_B,price_C,price_separate,price_react,t_max,dt)
    # second_order_reaction_A2_analysis(k,nA_initial,price_A,price_C,price_separate,price_react,t_max,dt)
    second_order_reaction_AB_analysis(k/nB_initial,nA_initial,nB_initial,price_A,price_B,price_C,price_separate,price_react,t_max,dt)


    #make figure
    plt.legend()
    plt.show()

def psuedo_first_order_reaction_analysis(K,NA_initial,NB_initial,Price_A,Price_B,Price_C,Price_separate,Price_react,T_max,Dt) :
    T_list = np.arange(0,T_max+Dt,Dt)
    NA = (NA_initial*np.exp(-K*T_list))
    NB = (NB_initial+NA_initial*(np.exp(-K*T_list)-1))
    NC = NA_initial*(1-np.exp(-K*T_list))
    C_profit = np.zeros(len(T_list))
    Produce_Cost = np.zeros(len(T_list))

    for T_index in range(len(T_list)) :
        T = T_list[T_index]
        Produce_Cost[T_index] = NA_initial*Price_A+NB_initial*Price_B+(NA[T_index]+NB[T_index])*Price_separate+Price_react*T
        C_profit[T_index] = NC[T_index]*Price_C - Produce_Cost[T_index]
        C_profit_max = np.max(C_profit)
    Profit_max_T = float((np.where(C_profit == C_profit_max)[0])*Dt)
    print("the maximum of C_profit is "+str(C_profit_max)+" that is when t is "+str(Profit_max_T))


    # plt.scatter(T_list,C_profit,label ="C_profit",s=0.01)
    # plt.scatter(Profit_max_T,C_profit_max,s=0.2,c="r")

    plt.scatter(T_list,NC,label="NC_pusuedo_A",s=0.01)
    plt.scatter(T_list,NA,label="NA_pusuedo_A",s=0.01)


def second_order_reaction_AB_analysis(K,NA_initial,NB_initial,Price_A,Price_B,Price_C,Price_separate,Price_react,T_max,Dt) :
    T_list = np.arange(0,T_max+Dt,Dt)
    if NA_initial == NB_initial :
        NC = NA_initial*(1-1/(K*NA_initial*T_list+1))
        NA = NA_initial - NC
        NB = NB_initial - NC

    else :
        NC = NA_initial*NB_initial*(1-np.exp(K*(NA_initial-NB_initial)*T_list))/(NB_initial-NA_initial*np.exp(K*(NA_initial-NB_initial)*T_list))
        NA = NA_initial - NC
        NB = NB_initial - NC

    C_profit = np.zeros(len(T_list))
    Produce_Cost = np.zeros(len(T_list))

    for T_index in range(len(T_list)) :
        T = T_list[T_index]
        Produce_Cost[T_index] = NA_initial*Price_A+NB_initial*Price_B+(NA[T_index]+NB[T_index])*Price_separate+Price_react*T
        C_profit[T_index] = NC[T_index]*Price_C - Produce_Cost[T_index]
        C_profit_max = np.max(C_profit)
    Profit_max_T = float((np.where(C_profit == C_profit_max)[0])*Dt)
    print("the maximum of C_profit is "+str(C_profit_max)+" that is when t is "+str(Profit_max_T))


    # plt.scatter(T_list,C_profit,label ="C_profit",s=0.01)
    # plt.scatter(Profit_max_T,C_profit_max,s=0.2,c="r")

    plt.scatter(T_list,NC,label="NC_AB",s=0.01)
    plt.scatter(T_list,NA,label="NA_AB",s=0.01)



def second_order_reaction_A2_analysis(K,NA_initial,Price_A,Price_C,Price_separate,Price_react,T_max,Dt) :
    T_list = np.arange(0,T_max+Dt,Dt)
    NA = NA_initial/(NA_initial*K*T_list+1)
    NC = (NA_initial - NA)/2
    C_profit = np.zeros(len(T_list))
    Produce_Cost = np.zeros(len(T_list))

    for T_index in range(len(T_list)) :
        T = T_list[T_index]
        Produce_Cost[T_index] = NA_initial*Price_A+(NA[T_index])*Price_separate+Price_react*T
        C_profit[T_index] = NC[T_index]*Price_C - Produce_Cost[T_index]
        C_profit_max = np.max(C_profit)
    Profit_max_T = float((np.where(C_profit == C_profit_max)[0])*Dt)
    print("the maximum of C_profit is "+str(C_profit_max)+" that is when t is "+str(Profit_max_T))


    # plt.scatter(T_list,C_profit,label ="C_profit",s=0.01)
    # plt.scatter(Profit_max_T,C_profit_max,s=0.2,c="r")
    plt.scatter(T_list,NC,label="NC_A2",s=0.01)
    plt.scatter(T_list,NA,label="NA_A2",s=0.01)



if __name__ == '__main__':
    main()