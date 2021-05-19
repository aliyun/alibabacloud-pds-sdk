// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SystemTag extends TeaModel {
    @NameInMap("confidence")
    public Double confidence;

    @NameInMap("en_name")
    public String enName;

    @NameInMap("name")
    public String name;

    @NameInMap("parent_en_name")
    public String parentEnName;

    @NameInMap("parent_name")
    public String parentName;

    @NameInMap("source")
    public String source;

    @NameInMap("tag_level")
    public Long tagLevel;

    public static SystemTag build(java.util.Map<String, ?> map) throws Exception {
        SystemTag self = new SystemTag();
        return TeaModel.build(map, self);
    }

    public SystemTag setConfidence(Double confidence) {
        this.confidence = confidence;
        return this;
    }
    public Double getConfidence() {
        return this.confidence;
    }

    public SystemTag setEnName(String enName) {
        this.enName = enName;
        return this;
    }
    public String getEnName() {
        return this.enName;
    }

    public SystemTag setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

    public SystemTag setParentEnName(String parentEnName) {
        this.parentEnName = parentEnName;
        return this;
    }
    public String getParentEnName() {
        return this.parentEnName;
    }

    public SystemTag setParentName(String parentName) {
        this.parentName = parentName;
        return this;
    }
    public String getParentName() {
        return this.parentName;
    }

    public SystemTag setSource(String source) {
        this.source = source;
        return this;
    }
    public String getSource() {
        return this.source;
    }

    public SystemTag setTagLevel(Long tagLevel) {
        this.tagLevel = tagLevel;
        return this;
    }
    public Long getTagLevel() {
        return this.tagLevel;
    }

}
