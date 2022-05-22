import random




quotes = [
"extremely credible source' has called my office and told me that Barack Obama's birth certificate is a fraud.",
"I think if this country gets any kinder or gentler, it's literally going to cease to exist.",
"I think I could have stopped it because I have very tough illegal immigration policies, and people aren't coming into this country unless they're vetted and vetted properly. *Discussing 9/11*",
"I have a great relationship with African Americans, as you possibly have heard. I just have great respect for them. And they like me. I like them.",
"It's really cold outside, they are calling it a major freeze, weeks ahead of normal. Man, we could use a big fat dose of global warming!",
"The concept of global warming was created by and for the Chinese in order to make U.S. manufacturing non-competitive.",
"If Hillary Clinton can't satisfy her husband what makes her think she can satisfy America?",
"I never attacked him on his looks, and believe me, there's plenty of subject matter right there. *Rand Paul*",
"{John McCain is}... not a war hero. He's a war hero - he's a war hero 'cause he was captured. I Like people that weren't captured, OK, I hate to tell you.",
"Sorry losers and haters, but my IQ is one of the highest - and you all know it! Please don't feel so stupid or insecure, it's not your fault.",
"All of the women on The Apprentice flirted with me - consciously or unconsciously. That's to be expected.",
"I could stand in the middle of 5th Avenue and shoot somebody and I wouldn't lose voters.",
"Nobody has better respect for intelligence than Donald Trump.",
"Nobody knew health care could be so complicated.",
"I’m the least racist person you have ever interviewed.",
"Despite the constant negative press covfefe",
"“We have {Covid} totally under control. It’s one person coming in from China. It’s going to be just fine.”",
"We are up BIG, but they are trying to STEAL the Election. We will never let them do it. Votes cannot be cast after the Polls are closed!",
"We're doing so well after the plague. It's going away - June 2020",
"Within a couple of days, {infections are} going to be down to close to zero. One day, it’s like a miracle. It will disappear. - March 2020",
"if she gets to pick her judges, nothing you can do, folks. Although the second amendment people, maybe there is, I don’t know. But I’ll tell you what, that will be a horrible day.",
"I’ve said if Ivanka weren’t my daughter, perhaps I’d be dating her.",
"if you go out and buy groceries, you need a picture on a card—you need ID.",
"The noise {from windmills} causes cancer",
"You know, when I was running, 2016, Christmas was like you couldn't say the word. I said the word. And I said we're going to bring back Christmas, and we're going to be saying Christmas.",
"Why can’t we use nuclear weapons?",
"Russia, if you’re listening, I hope you’re able to find the 30,000 emails that are missing. I think you will probably be rewarded mightily by our press.",
"I’ve been treated very unfairly by this judge. Now, this judge is of Mexican heritage. I'm building a wall, OK? I'm building a wall.",
"Women: You have to treat them like s**t.",
"We won with poorly educated. I love the poorly educated.",
"Hillary Clinton…started the birther controversy. I finished it.",
"{The Trump Building} was the second-tallest building in downtown Manhattan...And now it’s the tallest. -September 11, 2001 ",
"There may be somebody with tomatoes in the audience. If you see somebody getting ready to throw a tomato, knock the crap out of them, would you? Seriously. OK? Just knock the hell—I promise you, I will pay for the legal fees.",
"Look at my African-American over here!"
"Happy Cinco de Mayo! The best taco bowls are made in Trump Tower Grill. I love Hispanics!"
"Look at that face! Would anyone vote for that? Can you imagine that, the face of our next president I mean, she's a woman, and I'm not supposed to say bad things, but really, folks, come on. Are we serious?"
]



def give_rand_quote():
    index = random.randrange(0, len(quotes))
    return quotes[index]

