using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class volumeChange : MonoBehaviour
{
    // Start is called before the first frame update
    public MyListener script;
    private Vector3 scaleChange;
    private Vector3 myVector;
    private float Number;
    private float accumulate;
    private float parameter;

    void Start()
    {

    }

    void Awake()
    {
        scaleChange = new Vector3(1f, 1f, 1f);
    }


    // Update is called once per frame
    void Update()
    {
        parameter = MyListener.variable;
        accumulate += 0.03f;
        Number = (Mathf.Sin(6*parameter) + 1) / 40 + 1;

        myVector = new Vector3(Number, Number, 1f);
        Debug.Log(parameter);

        transform.localScale = myVector;

        //if (Input.GetKey(KeyCode.RightArrow))
        //{

        //transform.localScale =myVector;
        //}
    }
}