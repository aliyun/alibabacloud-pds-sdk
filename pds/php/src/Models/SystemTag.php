<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class SystemTag extends Model
{
    /**
     * @var int
     */
    public $confidence;

    /**
     * @var string
     */
    public $enName;

    /**
     * @var string
     */
    public $name;

    /**
     * @var string
     */
    public $parentEnName;

    /**
     * @var string
     */
    public $parentName;

    /**
     * @var bool
     */
    public $selected;

    /**
     * @var int
     */
    public $tagLevel;
    protected $_name = [
        'confidence'   => 'confidence',
        'enName'       => 'en_name',
        'name'         => 'name',
        'parentEnName' => 'parent_en_name',
        'parentName'   => 'parent_name',
        'selected'     => 'selected',
        'tagLevel'     => 'tag_level',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->confidence) {
            $res['confidence'] = $this->confidence;
        }
        if (null !== $this->enName) {
            $res['en_name'] = $this->enName;
        }
        if (null !== $this->name) {
            $res['name'] = $this->name;
        }
        if (null !== $this->parentEnName) {
            $res['parent_en_name'] = $this->parentEnName;
        }
        if (null !== $this->parentName) {
            $res['parent_name'] = $this->parentName;
        }
        if (null !== $this->selected) {
            $res['selected'] = $this->selected;
        }
        if (null !== $this->tagLevel) {
            $res['tag_level'] = $this->tagLevel;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return SystemTag
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['confidence'])) {
            $model->confidence = $map['confidence'];
        }
        if (isset($map['en_name'])) {
            $model->enName = $map['en_name'];
        }
        if (isset($map['name'])) {
            $model->name = $map['name'];
        }
        if (isset($map['parent_en_name'])) {
            $model->parentEnName = $map['parent_en_name'];
        }
        if (isset($map['parent_name'])) {
            $model->parentName = $map['parent_name'];
        }
        if (isset($map['selected'])) {
            $model->selected = $map['selected'];
        }
        if (isset($map['tag_level'])) {
            $model->tagLevel = $map['tag_level'];
        }

        return $model;
    }
}
