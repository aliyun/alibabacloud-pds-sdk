<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class DeleteDriveModel extends Model {
    protected $_name = [
        'headers' => 'headers',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return DeleteDriveModel
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        return $model;
    }
    /**
     * @var string[]
     */
    public $headers;

}
