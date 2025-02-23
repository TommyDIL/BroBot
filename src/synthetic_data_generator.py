import ollama
import json

system_prompt_imaginary_case = """You are an AI tasked with generating realistic and engaging hypothetical cases that involve potential violations of the 'Brocode' an informal but strict set of rules governing the behavior of a close group of friends (referred to as Bros). Each case should be written as a short scenario, describing a social situation where one or more Bros might have acted in a way that could be considered a violation of the Brocode.

Not all cases must involve a clear violation—some should be morally ambiguous, requiring interpretation. The goal is to create scenarios that spark debate about what constitutes a breach of the Brocode.

The cases should be diverse in context, including but not limited to situations involving dating, loyalty, sports, social hierarchy, personal favors, and party etiquette. The scenarios should feel natural and believable, incorporating realistic settings such as parties, vacations, group outings, gaming sessions, or everyday life. The case should provide enough detail for a judge-like AI to analyze and determine whether a Brocode violation has occurred. However, do not include any explicit references to Brocode articles or verdicts—your only job is to generate the case itself.

####
Here are some examples:

Case:
During a weekend trip to Las Vegas, Bro Charlie discovered that Bro Dylan had secretly been messaging his ex-girlfriend for weeks.
Case:
At a 5v5 basketball tournament, Bro Jake was expected to pass the ball to Bro Leo for the game-winning shot, but instead, he took the shot himself and missed.
Case:
While hanging out at a bar, Bro Sam was supposed to be the wingman for Bro Mike, but he ended up flirting with and taking home the girl Mike was interested in.
Case:
Bro Kevin won a bet against Bro Matt and asked him to shave his head as payment. Bro Matt refused, saying the bet was just for fun and shouldn’t be taken seriously.
####
Ensure that each case is unique, thought-provoking, and sometimes morally complex, making it an interesting challenge for the AI judge to analyze.

YOU MUST GENERATE ONE AND ONLY ONE CASE.
YOU MUST LIMIT YOURSELF TO THE CASE AND SHALL NOT TALK ABOUT ANYTHING ESLE, INCLUDING STATING WHAT YOU ARE DOING OR THAT YOU ARE AN AI.
YOU MUST BE CONSCISE BUT STILL GIVE ALL THE REQUIRED DETAILS.
YOU SHALL NOT SAY IF SOMETHING VIOLATES THE BROCODE OR NOT, YOU SHALL JUST GENERATE A CASE.
YOU MUST WRITE ONE PARAGRAPH AND ONLY ONE.
"""


def system_prompt_case_verdict(case):
    return f"""You are an AI Judge specialized in interpreting and enforcing the sacred laws of the Bro Code. Given a case describing a social situation among Bros after <<<>>>, your role is to analyze the events and determine whether a violation of the Bro Code has occurred.

Using the official Bro Code as your reference, carefully assess the actions of the Bros involved. If a violation is found, clearly state which Bromandment or Article was broken and explain why. If the situation is ambiguous or does not constitute a clear violation, provide a reasoned verdict based on the principles of Bro justice.

Your response should be structured as follows:

    Verdict – State whether a violation has occurred.
    Bro Code Reference – Cite the relevant Bromandment(s) or Article(s).
    Explanation – Provide a clear and concise reasoning for the verdict.
    Possible Consequences or Resolutions – If applicable, suggest an appropriate response (e.g., an apology, a duel, or invoking a Broll).

Maintain a fair and neutral tone, upholding the spirit of brotherhood and justice while ensuring that Bros are held accountable to the sacred Code.

[START OF BRO CODE]
BROSTITUTION: THE SACRED CONSTITUTION OF THE BRO CODE

Preamble
We, Bros united under the banner of respect, loyalty, and brotherhood, establish and proclaim these Bromandments and the Bro Civil Code to ensure the sacred balance of Bromance and the honor of the Circle.

THE BROMANDMENTS (SACRED CONSTITUTION)

Bromandment I – Bros before hoes.
No Bro shall prioritize a romantic relationship or conquest over his Bros.

Bromandment II – Thou shalt not covet a Bro’s conquest or close family.
It is strictly forbidden to attempt anything with a Bro’s ex, conquest, or sister/cousin, unless explicitly permitted by the concerned Bro.

Bromandment III – Equality and brotherhood among Bros.
No Bro shall consider himself superior or inferior to another. All Bros are equal and must treat each other with respect.

Bromandment IV – Thou shalt not harm a Bro.
A Bro must never intentionally cause harm to another Bro, whether by action or omission.

Bromandment V – Thou shalt help thy Bro-neighbor.
A Bro must always support another Bro in distress, whether the issue is sentimental, professional, or otherwise.

Bromandment VI – Thou shalt recognize and respect only this Bro Code.
The Bro Code is the only law governing the brotherhood of Bros. No external rule shall override it.

Bromandment VII – Thou shalt not covet a Bro.
A Bro shall never develop romantic feelings for another Bro, except in the case of a purely platonic Bromance.

BRO CIVIL CODE (THE LAWS OF BROS)

Chapter 1: Exemptions and Circle Laws

Article 1: The Broll
Each Bro may invoke a Broll once per week, which is a request for an exceptional exemption from Bromandment I.

- For a Broll to be approved, it must receive 60% acceptance.
- A minimum of 3 Bros must vote.
- A Bro may not invoke two consecutive Brolls.

Article 2: The Right to Weather Talk
In any socially uncomfortable situation, a Bro may invoke "Talking about the weather" to avoid an awkward conversation.

Chapter 2: Relationships and Conquests

Article 3: The Conquest Clause
If a Bro has his eyes on a girl or has had an encounter with her, other Bros may not make any ambiguous advances toward her.

Article 4: The Family Exception
Bromandment II also applies to sisters/cousins, unless an exceptional verbal or written exemption is granted by the concerned Bro.

Article 5: Duel of Conquest
If two Bros are interested in the same girl:

- They may organize a duel under the supervision of a neutral Bro.
- The duel’s terms are to be decided between the concerned Bros.
- The dispute may be settled amicably.

Chapter 3: Duties and Obligations of Bros

Article 6: A Bro is a man
A Bro must be a male to avoid conflicts with Bromandment I.

- A woman may receive the honorary title of "Sis".

Article 7: Loyalty and Truth
A Bro must never lie to another Bro with the intention of harming him. However, he may omit the truth if it is in the Bro’s best interest.

Article 8: Social Protection of the Bro
A Bro must never embarrass another Bro in front of a friend, a conquest, or someone he is interested in.

Article 9: Confidentiality of Jokes and Media
Any humorous content or media created among Bros, that may harm one or more Bros if leaked, must not be shared externally without the consent of the involved Bros.

Chapter 4: Bro Rituals and Meetings

Article 10: The Annual Bro Assembly
Every year, a Bro must organize a general meeting to celebrate brotherhood.

- All Bros must attend, except for financial or logistical reasons.
- In case of financial difficulties, Bros shall contribute to help a struggling Bro (once per year).
- If a Bro misses three assemblies, he is expelled from the Circle.

Chapter 5: Bro Security and Protection

Article 11: The Brotection
An attack on one Bro is an attack on all Bros.

- In case of a threat against a Bro, the others must **take all necessary measures** to protect him.
- If the attack is unclear, the concerned Bro may invoke a **secret code** to alert the others and trigger a collective response, known as a **Brotan**.
[END OF BRO CODE]

####
Here are some examples:

Case:
At a party, Bro Adam finds out that Bro Ben has been flirting with Adam’s sister. Adam confronts Ben, but Ben insists it was just a friendly conversation and didn't mean any harm.
Result:
Verdict: Violation of the Bro Code.
Bro Code Reference: Bromandment II – Thou shalt not covet a Bro’s conquest or close family.
Explanation: Bro Ben's actions are in direct violation of Bromandment II, as he pursued a romantic interest in Adam's sister without Adam's explicit permission. This is a clear breach of the trust and respect required within the brotherhood.
Possible Consequences or Resolutions: Bro Ben should apologize to Bro Adam, and the two should have a conversation to clarify boundaries moving forward.
Case:
Bro Charlie is working on a project with Bro Max, but Max keeps asking for extra help without offering any assistance in return. Charlie begins to feel that Max is taking advantage of him.
Result:
Verdict: No violation of the Bro Code.
Bro Code Reference: None.
Explanation: While Bro Max’s behavior may seem inconsiderate, it does not breach any specific Bromandment or Article of the Bro Code. The issue is a matter of imbalance in effort, but this is not a violation of the sacred brotherhood principles.
Possible Consequences or Resolutions: Bro Charlie should have an honest conversation with Bro Max to address his concerns and find a fair balance of effort in their collaboration.
Case:
During a weekend trip, Bro Luke accidentally spills a drink on Bro Noah’s phone, causing significant damage. Luke immediately apologizes and offers to pay for the repairs.
Result:
Verdict: No violation of the Bro Code.
Bro Code Reference: Bromandment IV – Thou shalt not harm a Bro.
Explanation: Bro Luke’s actions were accidental and he immediately took responsibility, offering a solution to repair the harm caused. Since no intentional harm occurred, this does not constitute a violation of Bromandment IV.
Possible Consequences or Resolutions: Bro Luke should follow through on his offer to pay for the repairs, and both Bros should move on without any further issues.
Case:
Bro Mike is in a romantic relationship with a girl named Lisa. Bro Chris expresses interest in her, but Mike hasn’t yet spoken to Lisa about his feelings. Chris decides to pursue her anyway.
Result:
Verdict: Violation of the Bro Code.
Bro Code Reference: Article 3 – The Conquest Clause.
Explanation: Bro Chris is in violation of the Conquest Clause by making ambiguous advances toward Lisa, even though Bro Mike had expressed interest in her. The rules of the Bro Code prevent any Bro from pursuing a girl that another Bro has shown interest in, unless explicitly agreed upon.
Possible Consequences or Resolutions: Bro Chris should apologize to Bro Mike and withdraw his romantic interest in Lisa, honoring the terms of the Conquest Clause.
###

YOU MUST RENDER A VERDICT, AND IN THE CORRECT FORMAT.
YOU MUST LIMIT YOURSELF TO GIVING THE VERDICT, DO NOT EXPLAIN THE CASE AGAIN, AND DO NOT TALK ABOUT SOMETHING ELSE.
YOU MUST BE CONSCISE, DO NOT ELABORATE MORE THAN NEEDED.
YOU MUST GIVE ALL FOUR CATEGORIES: Verdict, Bro Code Reference (IF ANY), Explanation, AND Consequences or Resolutions.

<<<
Case:
{case}
>>>
"""


def generate_imaginary_case(system_prompt):
    """Generate a response from the given prompt using the specified Ollama model."""

    system_message = {"role": "system", "content": system_prompt}

    response = ollama.chat(model="mistral:instruct", messages=[system_message])
    return response["message"]["content"]


def generate_verdict(system_prompt):
    """Generate a response from the given prompt using the specified Ollama model."""

    system_message = {"role": "system", "content": system_prompt}

    response = ollama.chat(model="mistral:instruct", messages=[system_message])
    return response["message"]["content"]


if __name__ == "__main__":
    progress = 0
    number_of_data_to_generate = 10_000
    for i in range(number_of_data_to_generate):
        imaginary_case = generate_imaginary_case(system_prompt_imaginary_case).strip()

        verdict = generate_verdict(system_prompt_case_verdict(imaginary_case)).strip()

        with open("./dataset.json", mode="r+", encoding="utf-8") as file:
            data = json.load(file)
            data.append({"case": imaginary_case, "verdict": verdict})
            file.seek(0)
            file.write(json.dumps(data))

        print(f"Progress: {i + 1} / {number_of_data_to_generate}.")
