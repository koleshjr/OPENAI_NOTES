#how llms are trained
""" 
Text generation process - prompt + completion. This was trained using
supervised learning to predict the next word

Base LLM -> Predicts next word, based on training data


InstructioN Tuned LLM -> Train a Base LLM on a lot of data
                    -> Fine tune on examples of where the output follows on input instruction

Obtain human - ratings of the quality of different LLM outputs 
on criteria such as whether it is helpful, honest and
harmless
Tune LLM to increase probability that it generates the more higly rated outputs(
using RLHF: Reinforcement Learning from Human Feedback
)

gpt3.5-turbo has 4000 tokens for input and output tokens

Supervised Learning: Get labelled data - Train Model On data - Deploy nd call model
Prompt Based AI - Specify Prompt -> Call Model


BUILDING AN LLM POWERED APPLICATION:

Tune prompts on handful of examples
Add additional "tricky" examples opportunistically
Develop metrics to measure performance on examples
Collect randomly sampled set of examples to tune to
(development set/ hold out cross validation set)-90 - 95v% perfomance
collect and use a hold out test set


Use a new llm to evaluate output of another llm
Compare the bots response to an expert response using rubric


"""