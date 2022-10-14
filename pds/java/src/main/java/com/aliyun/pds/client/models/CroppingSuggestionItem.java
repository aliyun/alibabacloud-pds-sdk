// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class CroppingSuggestionItem extends TeaModel {
    @NameInMap("aspect_ratio")
    public String aspectRatio;

    @NameInMap("cropping_boundary")
    public CroppingBoundary croppingBoundary;

    @NameInMap("score")
    public Double score;

    public static CroppingSuggestionItem build(java.util.Map<String, ?> map) throws Exception {
        CroppingSuggestionItem self = new CroppingSuggestionItem();
        return TeaModel.build(map, self);
    }

    public CroppingSuggestionItem setAspectRatio(String aspectRatio) {
        this.aspectRatio = aspectRatio;
        return this;
    }
    public String getAspectRatio() {
        return this.aspectRatio;
    }

    public CroppingSuggestionItem setCroppingBoundary(CroppingBoundary croppingBoundary) {
        this.croppingBoundary = croppingBoundary;
        return this;
    }
    public CroppingBoundary getCroppingBoundary() {
        return this.croppingBoundary;
    }

    public CroppingSuggestionItem setScore(Double score) {
        this.score = score;
        return this;
    }
    public Double getScore() {
        return this.score;
    }

}
