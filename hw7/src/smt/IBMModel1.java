package smt;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class IBMModel1 {

	// P(f|e) 
	private HashMap<String, HashMap<String, Double>> tt; 
	
	public IBMModel1(){
		
	}

	public IBMModel1(String modelFileName){
		tt = new HashMap<String, HashMap<String, Double>>();
		/* YOUR CODE HERE (PART III)
		 * TODO: Load the model from file
		 */

	}
	
	/*
	 * Initialize the translation with the co-occurrence counts
	 */
	public void initTranslationTable(ArrayList<ArrayList<String>> eSentences, ArrayList<ArrayList<String>> fSentences){
		assert(eSentences.size() == fSentences.size());
		int numSentences = eSentences.size();

		tt = new HashMap<String, HashMap<String,Double>>();
		for (int j = 0; j < numSentences; j++) {
			ArrayList<String> eSentence = eSentences.get(j);
			ArrayList<String> fSentence = fSentences.get(j);
			for (String eWord : eSentence) {
				for (String fWord : fSentence){
					Util.incrementCount(tt, eWord, fWord, 1);
				}
			}
		}
		normalizeTranslationTable(tt);
	}
	

	
	public void train(ArrayList<ArrayList<String>> eSentences, ArrayList<ArrayList<String>> fSentences, int maxIterations){
		initTranslationTable(eSentences, fSentences);
		assert(eSentences.size() == fSentences.size());
		int numSentences = eSentences.size();
        HashMap<String, HashMap<String, Double>> newTT;
        double prevDataLogLikelihood = Double.NEGATIVE_INFINITY;
		for (int i = 0; i < maxIterations; i++) {
			double totalDataLogLikelihood = 0.0;
			newTT = new HashMap<String, HashMap<String, Double>>();
			for (int j = 0; j < numSentences; j++) {
				ArrayList<String> eSentence = eSentences.get(j);
				ArrayList<String> fSentence = fSentences.get(j);
				/* YOUR CODE HERE (PART I)
				 * TODO: Implement the EM algorithm for IBM Model 1 here
				 * 1. Compute the expected count for each sentence pair store it in newTT
				 * 2. Update the totalDataLogLikelihood (sum log P(F|E) for all pairs)
				 * 
				 * The solution is only 10 lines of code.
				 */

			}
			System.out.println("iteration "+ i + " loglikelihood per sentence = " + totalDataLogLikelihood / numSentences);
			normalizeTranslationTable(newTT);
			tt = newTT;
			if ( i > 0 && (totalDataLogLikelihood - prevDataLogLikelihood) / numSentences < 0.01){
				break;
			}
			prevDataLogLikelihood = totalDataLogLikelihood;
		}

	}

	/*
	 * Normalize the translation table C(F,E) into a translation probability table P(F|E)
	 */
	public void normalizeTranslationTable(HashMap<String, HashMap<String, Double>> translationTable){
		for (String eWord : translationTable.keySet()){
			HashMap<String, Double> countTable = translationTable.get(eWord);
			double totalCount = 0.0;
			for (String fWord : countTable.keySet()){
				totalCount += countTable.get(fWord);
			}
			for (String fWord : countTable.keySet()){
				double unnormalizedCount = countTable.get(fWord);
				countTable.put(fWord, unnormalizedCount / totalCount);
				//System.out.println("P("+fWord+"|"+eWord+") = "+ unnormalizedCount/totalCount);
			}
		}
	}

	public double computeTranslationLogProbability(ArrayList<String> eSentenceHypothesis, ArrayList<String> fSentence) {
        /* YOUR CODE HERE (Part III)
         * TODO: Compute translation probability P(F|E) to score the hypothesis translation 
         * 
         * The solution is around 10 lines of code.
         */
	}
	
	public void save(String fileName){
		/* YOUR CODE HERE (Part III)
		 * TODO: saving the translation table onto a human-readable file
		 * Feel free to change the header if you want. 
		 * Sometimes it is easier to System.out.println it out and pipe the output to the file 
		 * if you work directly on the shell.
		 * 
		 * Use any format that you like. For example,
		 * ein buch 0.003
		 * book buch 0.08
		 */
	}
	
	
	public static void main(String[] argv) throws IOException{
		IBMModel1 model = new IBMModel1();
		model.train(Util.readCorpus("english.txt"), Util.readCorpus("german.txt"), 10);
	}
}
 
