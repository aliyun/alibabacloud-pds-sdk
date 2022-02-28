// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ActionItem extends TeaModel {
    @NameInMap("action")
    public String action;

    @NameInMap("effect")
    public String effect;

    @NameInMap("inherited")
    public Boolean inherited;

    @NameInMap("inherited_from")
    public String inheritedFrom;

    public static ActionItem build(java.util.Map<String, ?> map) throws Exception {
        ActionItem self = new ActionItem();
        return TeaModel.build(map, self);
    }

    public ActionItem setAction(String action) {
        this.action = action;
        return this;
    }
    public String getAction() {
        return this.action;
    }

    public ActionItem setEffect(String effect) {
        this.effect = effect;
        return this;
    }
    public String getEffect() {
        return this.effect;
    }

    public ActionItem setInherited(Boolean inherited) {
        this.inherited = inherited;
        return this;
    }
    public Boolean getInherited() {
        return this.inherited;
    }

    public ActionItem setInheritedFrom(String inheritedFrom) {
        this.inheritedFrom = inheritedFrom;
        return this;
    }
    public String getInheritedFrom() {
        return this.inheritedFrom;
    }

}
