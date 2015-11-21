//
//  FirstViewController.swift
//  FlirAir
//
//  Created by Neo on 11/21/15.
//  Copyright © 2015 padblish. All rights reserved.
//

import UIKit

class BodyViewController: UIViewController {

    @IBOutlet weak var buttonHead: UIButton!
    @IBOutlet weak var buttonTorso: UIButton!
    @IBOutlet weak var buttonLegs: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func buttonHead(sender: AnyObject) {
        buttonHead.setImage(UIImage(named: "head"), forState: UIControlState.Normal)
        buttonTorso.setImage(UIImage(named: "torso_b"), forState: UIControlState.Normal)
        buttonLegs.setImage(UIImage(named: "legs_b"), forState: UIControlState.Normal)
    }

    @IBAction func buttonTorso(sender: AnyObject) {
        buttonHead.setImage(UIImage(named: "head_b"), forState: UIControlState.Normal)
        buttonTorso.setImage(UIImage(named: "torso"), forState: UIControlState.Normal)
        buttonLegs.setImage(UIImage(named: "legs_b"), forState: UIControlState.Normal)
    }

    @IBAction func buttonLegs(sender: AnyObject) {
        buttonHead.setImage(UIImage(named: "head_b"), forState: UIControlState.Normal)
        buttonTorso.setImage(UIImage(named: "torso_b"), forState: UIControlState.Normal)
        buttonLegs.setImage(UIImage(named: "legs"), forState: UIControlState.Normal)
    }

}

