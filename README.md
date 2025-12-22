<img width="792" height="505" alt="image" src="https://github.com/user-attachments/assets/86543d4c-ecd7-4a0f-8d53-d4be76bdbdd8" /># A/B Testing - Simulation and Exploratory Data Analysis

This repository consists of an A/B test on difficulty flow analysis and exploratory data analysis on a game dataset. 

## Objective
Evaluate which variant (A/B) performs better in terms of:
- Daily Active Users (DAU)
- Total Revenue (Ads + IAP)
- Calculation of different total revenue scenarios
- Decision making

## Assumptions
- The purchase cost or average cost for an item did not given. So, I asssume that one item is 1 Dollar and the calculations was made by this assumption.
- Another assumption is that R(0) = 1, which means that the user who installs the game 100% enters the game. The calculations was made by this assumption.

## Methodology
- Cohort stacking (cumulative sum) approach
- Log-linear interpolation for not known retention points:  Markus Deserno’s article explains how linear and logarithmic interpolation extract precise numerical values from graphs by showing that logarithmic interpolation is equivalent to performing linear interpolation in log-space, yielding geometrically consistent estimates for exponentially scaled data. In this case, we have given detention points and there are missing or not given detention points. You will see that this approach will be conducted to our analyses.
- Complex problems divided into parts and solved like an algorithm solution. So when reader follows the solving, will read the solving easily.   

## Structure
- notebooks/: step-by-step analysis
- src/: reusable simulation and analytics functions
- README.md/: Graphs will be here
## Key Findings and Graphs

## Q1. a)
<img width="729" height="461" alt="1" src="https://github.com/user-attachments/assets/57f451e3-c3e6-4707-9fe1-20e394f5524d" />
After 15 days, as we can see from the line graph, most dail active players would be in the Variant B.

b)
<img width="792" height="505" alt="image" src="https://github.com/user-attachments/assets/e0c05307-c81d-4044-9646-bdf7b9460a2e" />
Variant A will earn more money than Variant B by the Day 15

c) 
<img width="878" height="513" alt="image" src="https://github.com/user-attachments/assets/c6ac30f2-924d-40c2-a515-39262d5106cb" />
By Day 30, Variant A still makes more money than Variant B because of Ad purchases makes more money than in-game purchasing.

d)
<img width="1061" height="615" alt="image" src="https://github.com/user-attachments/assets/58726154-3aa2-405f-af15-f6ae9f0cb88b" />
<img width="1019" height="547" alt="image" src="https://github.com/user-attachments/assets/d5ca73a9-8c1d-429e-9a4b-1cf3f3bf884a" />
<img width="1032" height="572" alt="image" src="https://github.com/user-attachments/assets/cd8f1ead-781a-43aa-9998-3a49d130201a" />
<img width="908" height="575" alt="image" src="https://github.com/user-attachments/assets/5aefde6d-ce73-45ce-88f3-320b232428e5" />

e)
<img width="846" height="510" alt="image" src="https://github.com/user-attachments/assets/a61014bc-81bf-4eb2-ad91-4682cc98777c" />
<img width="833" height="515" alt="image" src="https://github.com/user-attachments/assets/03f712f6-c8b2-4d64-856e-de30efae46dc" />

In this scenario, again, Variant A will earn more money than Variant B. Nearly all of the scenarios, Variant A was winning from the Ad purchasing and Variant B was winning for In-Game purchasing. Because Variant B has more Daily Active User (reminder for retention points) and this leads naturally more purchasing. Although, we should keep going with Variant A because it looks like Ad purchasing earns more than in-game purchasing.

f) The question is, "Which one should you prioritize, and why? (d or e)"

I would prioritize adding the new user source. Because of two reasons:

1- Mathematically, adding the new user source makes more money than 10-day sale action. ($119.451 > $119.251)

2- Heuristically, while 10-day sale would create a short-term hype and money, it would be temporary. On the other side, adding permanent new user source would go continious. As we can see the consequence, for another run, adding permanent source will be outplay the 10-day sale. And in the long term, we might be able to statistically test or analyze the effect of this action because we would have enough data in the long term for this action.




