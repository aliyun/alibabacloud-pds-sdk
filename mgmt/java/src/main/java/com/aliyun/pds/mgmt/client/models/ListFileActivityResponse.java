// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * list file activity response
 */
public class ListFileActivityResponse extends TeaModel {
    // Activities
    @NameInMap("activities")
    public java.util.List<FileActivity> activities;

    // NextMarker
    @NameInMap("next_marker")
    public String nextMarker;

    public static ListFileActivityResponse build(java.util.Map<String, ?> map) throws Exception {
        ListFileActivityResponse self = new ListFileActivityResponse();
        return TeaModel.build(map, self);
    }

    public ListFileActivityResponse setActivities(java.util.List<FileActivity> activities) {
        this.activities = activities;
        return this;
    }
    public java.util.List<FileActivity> getActivities() {
        return this.activities;
    }

    public ListFileActivityResponse setNextMarker(String nextMarker) {
        this.nextMarker = nextMarker;
        return this;
    }
    public String getNextMarker() {
        return this.nextMarker;
    }

}
