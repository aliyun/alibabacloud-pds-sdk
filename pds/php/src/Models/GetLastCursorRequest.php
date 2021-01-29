<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取最新游标
 */
class GetLastCursorRequest extends Model {
    protected $_name = [
        'driveId' => 'drive_id',
    ];
    public function validate() {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return GetLastCursorRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['drive_id'])){
            $model->driveId = $map['drive_id'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description drive_id
     * @example 1
     * @var string
     */
    public $driveId;

}
