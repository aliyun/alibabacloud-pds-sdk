<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class ImageMediaMetadata extends Model {
    protected $_name = [
        'height' => 'height',
        'width' => 'width',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->height) {
            $res['height'] = $this->height;
        }
        if (null !== $this->width) {
            $res['width'] = $this->width;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return ImageMediaMetadata
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['height'])){
            $model->height = $map['height'];
        }
        if(isset($map['width'])){
            $model->width = $map['width'];
        }
        return $model;
    }
    /**
     * @description height
     * @example 2448
     * @var int
     */
    public $height;

    /**
     * @description width：
     * @example 3264
     * @var int
     */
    public $width;

}
