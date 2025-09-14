using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Meditation : MonoBehaviour
{
    // Start is called before the first frame update
    private Vector3 scaleChange;
    private Vector3 myVector;
    private float Number;
    private float accumulate;
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
        accumulate += 0.01f;
        Number = (Mathf.Sin(accumulate) + 1) / 8 + 10;

        myVector = new Vector3(Number, Number, 1f);
        Debug.Log(Number);

        transform.localScale = myVector;

        //if (Input.GetKey(KeyCode.RightArrow))
        //{

        //transform.localScale =myVector;
        //}
    }
}