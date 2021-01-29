<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class DataCName extends Model {
    protected $_name = [
        'dataCname' => 'data_cname',
        'location' => 'location',
    ];
    public function validate() {
        Model::validateRequired('dataCname', $this->dataCname, true);
        Model::validateRequired('location', $this->location, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->dataCname) {
            $res['data_cname'] = $this->dataCname;
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return DataCName
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['data_cname'])){
            $model->dataCname = $map['data_cname'];
        }
        if(isset($map['location'])){
            $model->location = $map['location'];
        }
        return $model;
    }
    /**
     * @description datacname
     * @example pdsdata-cn-hangzhou.yoursite.com
     * @var string
     */
    public $dataCname;

    /**
     * @description data location
     * @example cn-hangzhou
     * @var string
     */
    public $location;

}
