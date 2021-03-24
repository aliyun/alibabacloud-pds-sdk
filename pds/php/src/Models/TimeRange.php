<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class TimeRange extends Model
{
    /**
     * @description EndTime
     *
     * @example ""
     *
     * @var string
     */
    public $endTime;

    /**
     * @description StartTime
     *
     * @example ""
     *
     * @var string
     */
    public $startTime;
    protected $_name = [
        'endTime'   => 'end_time',
        'startTime' => 'start_time',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->endTime) {
            $res['end_time'] = $this->endTime;
        }
        if (null !== $this->startTime) {
            $res['start_time'] = $this->startTime;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return TimeRange
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['end_time'])) {
            $model->endTime = $map['end_time'];
        }
        if (isset($map['start_time'])) {
            $model->startTime = $map['start_time'];
        }

        return $model;
    }
}
