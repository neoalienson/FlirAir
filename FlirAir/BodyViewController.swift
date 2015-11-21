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
    
    func request(mode: String) {
        let url = NSURL(string: "http://flir.hopto.org:8000/" + mode)
        
        let task = NSURLSession.sharedSession().dataTaskWithURL(url!) {(data, response, error) in
            print("error")
        }
        
        task.resume()
    }
    
    @IBAction func buttonUp(sender: AnyObject) {
        let button = sender as! UIButton
        buttonHead.setImage(UIImage(named: ((button == buttonHead) ? "head" : "head_b")),
            forState: UIControlState.Normal)
        buttonTorso.setImage(UIImage(named: (button == buttonTorso) ? "torso" : "torso_b"),
            forState: UIControlState.Normal)
        buttonLegs.setImage(UIImage(named: (button == buttonLegs) ? "legs" : "legs_b"),
            forState: UIControlState.Normal)
        
        switch (button) {
        case buttonHead:
            request("head")
            break
        case buttonHead:
            request("torso")
            break
        case buttonHead:
            request("legs")
            break
        default:
            break
            
        }
    }

}

