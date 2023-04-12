import java.io.File;
import java.io.FileReader;
import java.io.IOException;

import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;


public class JsonEx11{
	public static void main(String[] args)throws IOException, ParseException {
		
		String data_directory = "c:/남서울대/2022 졸작-캡스톤/2020-02-062.도로장애물표면인지(광역시등)_sample/062.도로장애물-표면인지영상(광역시 등)_샘플_라벨링데이터/";
		File dir = new File(data_directory);
		
		String[] filenames = dir.list();
		
		for(String filename : filenames) {
				
		JSONParser parser = new JSONParser();
		
		try {
			FileReader reader = new FileReader(data_directory+filename);
			Object obj = parser.parse(reader);
			
			JSONObject jsonMain = (JSONObject)obj;
			JSONArray jsonArr = (JSONArray)jsonMain.get("annotations");
									
			for(int i=0; i<1; i++) {
				JSONObject jsonObj = (JSONObject)jsonArr.get(i);
							
				if(Integer.parseInt(String.valueOf(jsonObj.get("category_id"))) == 8)		
					System.out.println(filename);
					 
			}
			
		} catch (IOException | ParseException e) {
			e.printStackTrace();
			
				}
			}
		}
	}